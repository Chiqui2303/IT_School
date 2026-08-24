
import csv
import tkinter as tk
from datetime import datetime
from tkinter import filedialog, messagebox, ttk

import psycopg2
from psycopg2.extras import RealDictCursor



APP_TITLE = "Gestiune obiective de curățenie"
DEFAULT_TODO_TASKS = (
    "Îndepărtat păianjeni",
    "Șters praful",
    "Aspirat pardoseli",
    "Spălat pardoseli",
    "Igienizat baie",
    "Igienizat bucătărie",
    "Spălat vase",
    "Completat consumabile",
    "Odorizat",
    "Ventilat spațiul",
)
WEEKDAYS = ("Luni", "Marți", "Miercuri", "Joi", "Vineri", "Sâmbătă", "Duminică")


def parse_number(value: str, field_name: str, *, integer: bool = False) -> float | int | None:
    cleaned = value.strip().replace(" ", "").replace(",", ".")
    if not cleaned:
        return None
    try:
        number = float(cleaned)
    except ValueError as exc:
        raise ValueError(f"Câmpul «{field_name}» trebuie să conțină un număr.") from exc
    if number < 0:
        raise ValueError(f"Câmpul «{field_name}» nu poate fi negativ.")
    if integer:
        if not number.is_integer():
            raise ValueError(f"Câmpul «{field_name}» trebuie să fie un număr întreg.")
        return int(number)
    return number


def format_number(value: float | int | None) -> str:
    if value is None:
        return ""
    number = float(value)
    if number.is_integer():
        return str(int(number))
    return f"{number:.2f}".rstrip("0").rstrip(".")


class Database:
    def __init__(self) -> None:

        self.connection = psycopg2.connect(
                                host='localhost',
                                database='postgres',
                                user='postgres',
                                password='Sorin',
                                port='5433',
                                cursor_factory=RealDictCursor)
        try:
            self._create_schema()
        except Exception:
            self.connection.close()
            raise

    def _create_schema(self) -> None:
        schema = """
            CREATE TABLE IF NOT EXISTS objectives (
                id BIGSERIAL PRIMARY KEY,
                company_name TEXT NOT NULL,
                address TEXT NOT NULL DEFAULT '',
                location_area DOUBLE PRECISION,
                contract_start_date TEXT NOT NULL DEFAULT '',
                contract_value DOUBLE PRECISION,
                contact_person TEXT NOT NULL DEFAULT '',
                contact_details TEXT NOT NULL DEFAULT '',
                cleaning_agent_name TEXT NOT NULL DEFAULT '',
                cleaning_agent_contact TEXT NOT NULL DEFAULT '',
                cleaning_agent_salary DOUBLE PRECISION,
                intervention_weekdays TEXT NOT NULL DEFAULT '',
                intervention_duration_hours DOUBLE PRECISION,
                updated_at TEXT NOT NULL
            );

            ALTER TABLE objectives
                ADD COLUMN IF NOT EXISTS intervention_weekdays TEXT NOT NULL DEFAULT '';

            CREATE TABLE IF NOT EXISTS materials (
                id BIGSERIAL PRIMARY KEY,
                objective_id BIGINT NOT NULL,
                material_name TEXT NOT NULL,
                needed DOUBLE PRECISION NOT NULL DEFAULT 0,
                stock DOUBLE PRECISION NOT NULL DEFAULT 0,
                to_order DOUBLE PRECISION NOT NULL DEFAULT 0,
                FOREIGN KEY (objective_id) REFERENCES objectives(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS equipment (
                id BIGSERIAL PRIMARY KEY,
                objective_id BIGINT NOT NULL,
                equipment_name TEXT NOT NULL,
                good_condition BOOLEAN NOT NULL DEFAULT TRUE,
                needs_replacement BOOLEAN NOT NULL DEFAULT FALSE,
                FOREIGN KEY (objective_id) REFERENCES objectives(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS consumables (
                id BIGSERIAL PRIMARY KEY,
                objective_id BIGINT NOT NULL,
                consumable_name TEXT NOT NULL,
                needed DOUBLE PRECISION NOT NULL DEFAULT 0,
                stock DOUBLE PRECISION NOT NULL DEFAULT 0,
                to_order DOUBLE PRECISION NOT NULL DEFAULT 0,
                FOREIGN KEY (objective_id) REFERENCES objectives(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS objective_particularities (
                objective_id BIGINT PRIMARY KEY,
                content TEXT NOT NULL DEFAULT '',
                FOREIGN KEY (objective_id) REFERENCES objectives(id) ON DELETE CASCADE
            );

            CREATE TABLE IF NOT EXISTS objective_todos (
                id BIGSERIAL PRIMARY KEY,
                objective_id BIGINT NOT NULL,
                task_order INTEGER NOT NULL,
                task_name TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT FALSE,
                UNIQUE (objective_id, task_order),
                FOREIGN KEY (objective_id) REFERENCES objectives(id) ON DELETE CASCADE
            );
            """
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute(schema)

    def _fetchall(self, query: str, parameters: tuple[object, ...] = ()) -> list[dict[str, object]]:
        with self.connection.cursor() as cursor:
            cursor.execute(query, parameters)
            return list(cursor.fetchall())

    def _fetchone(
        self, query: str, parameters: tuple[object, ...] = ()
    ) -> dict[str, object] | None:
        with self.connection.cursor() as cursor:
            cursor.execute(query, parameters)
            return cursor.fetchone()

    def list_objectives(self) -> list[dict[str, object]]:
        return self._fetchall(
            """
            SELECT id, company_name, address
            FROM objectives
            ORDER BY LOWER(company_name), company_name
            """
        )

    def get_objective(self, objective_id: int) -> dict[str, object] | None:
        return self._fetchone("SELECT * FROM objectives WHERE id = %s", (objective_id,))

    def get_materials(self, objective_id: int) -> list[dict[str, object]]:
        return self._fetchall(
            "SELECT * FROM materials WHERE objective_id = %s ORDER BY id", (objective_id,)
        )

    def get_equipment(self, objective_id: int) -> list[dict[str, object]]:
        return self._fetchall(
            "SELECT * FROM equipment WHERE objective_id = %s ORDER BY id", (objective_id,)
        )

    def get_consumables(self, objective_id: int) -> list[dict[str, object]]:
        return self._fetchall(
            "SELECT * FROM consumables WHERE objective_id = %s ORDER BY id", (objective_id,)
        )

    def get_particularities(self, objective_id: int) -> str:
        row = self._fetchone(
            "SELECT content FROM objective_particularities WHERE objective_id = %s", (objective_id,)
        )
        return str(row["content"]) if row else ""

    def get_todos(self, objective_id: int) -> list[dict[str, object]]:
        return self._fetchall(
            """
            SELECT task_name, completed
            FROM objective_todos
            WHERE objective_id = %s
            ORDER BY task_order
            """,
            (objective_id,),
        )

    def save_all(
        self,
        objective_id: int | None,
        objective: dict[str, object],
        materials: list[tuple[str, float, float, float]],
        equipment: list[tuple[str, bool, bool]],
        consumables: list[tuple[str, float, float, float]],
        particularities: str,
        todos: list[tuple[str, bool]],
    ) -> int:
        columns = list(objective)
        with self.connection:
            with self.connection.cursor() as cursor:
                if objective_id is None:
                    placeholders = ", ".join("%s" for _ in columns)
                    cursor.execute(
                        f"""
                        INSERT INTO objectives ({', '.join(columns)})
                        VALUES ({placeholders})
                        RETURNING id
                        """,
                        tuple(objective[column] for column in columns),
                    )
                    inserted = cursor.fetchone()
                    if inserted is None:
                        raise psycopg2.DatabaseError("PostgreSQL nu a returnat ID-ul obiectivului.")
                    objective_id = int(inserted["id"])
                else:
                    assignments = ", ".join(f"{column} = %s" for column in columns)
                    cursor.execute(
                        f"UPDATE objectives SET {assignments} WHERE id = %s",
                        tuple(objective[column] for column in columns) + (objective_id,),
                    )

                cursor.execute("DELETE FROM materials WHERE objective_id = %s", (objective_id,))
                cursor.executemany(
                    """
                    INSERT INTO materials
                        (objective_id, material_name, needed, stock, to_order)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    ((objective_id, *row) for row in materials),
                )

                cursor.execute("DELETE FROM equipment WHERE objective_id = %s", (objective_id,))
                cursor.executemany(
                    """
                    INSERT INTO equipment
                        (objective_id, equipment_name, good_condition, needs_replacement)
                    VALUES (%s, %s, %s, %s)
                    """,
                    ((objective_id, *row) for row in equipment),
                )

                cursor.execute("DELETE FROM consumables WHERE objective_id = %s", (objective_id,))
                cursor.executemany(
                    """
                    INSERT INTO consumables
                        (objective_id, consumable_name, needed, stock, to_order)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    ((objective_id, *row) for row in consumables),
                )

                cursor.execute(
                    """
                    INSERT INTO objective_particularities (objective_id, content)
                    VALUES (%s, %s)
                    ON CONFLICT (objective_id) DO UPDATE SET content = EXCLUDED.content
                    """,
                    (objective_id, particularities),
                )

                cursor.execute("DELETE FROM objective_todos WHERE objective_id = %s", (objective_id,))
                cursor.executemany(
                    """
                    INSERT INTO objective_todos
                        (objective_id, task_order, task_name, completed)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (
                        (objective_id, task_order, task_name, completed)
                        for task_order, (task_name, completed) in enumerate(todos)
                    ),
                )
        return objective_id

    def delete_objective(self, objective_id: int) -> None:
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM objectives WHERE id = %s", (objective_id,))

    def close(self) -> None:
        self.connection.close()


class CleaningManagementApp(tk.Tk):
    OBJECTIVE_FIELDS = (
        ("company_name", "Denumire firmă *"),
        ("address", "Adresă"),
        ("location_area", "Suprafață locație (m²)"),
        ("contract_start_date", "Data începere contract (AAAA-LL-ZZ)"),
        ("contract_value", "Valoare contract (lei)"),
        ("contact_person", "Persoană de legătură"),
        ("contact_details", "Date contact persoană"),
        ("cleaning_agent_name", "Nume agent de curățenie"),
        ("cleaning_agent_contact", "Date contact agent"),
        ("cleaning_agent_salary", "Salariu agent curățenie (lei)"),
        ("intervention_duration_hours", "Durata intervenției (ore)"),
    )

    def __init__(self, database: Database) -> None:
        super().__init__()
        self.title(APP_TITLE)
        self.geometry("1180x760")
        self.minsize(940, 640)
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.db = database
        self.current_objective_id: int | None = None
        self.objective_choices: list[tuple[int, str]] = []
        self.objective_vars = {name: tk.StringVar() for name, _ in self.OBJECTIVE_FIELDS}
        self.weekday_vars = {day: tk.BooleanVar(value=False) for day in WEEKDAYS}
        self.material_vars = {
            "name": tk.StringVar(),
            "needed": tk.StringVar(),
            "stock": tk.StringVar(),
        }
        self.consumable_vars = {
            "name": tk.StringVar(),
            "needed": tk.StringVar(),
            "stock": tk.StringVar(),
        }
        self.equipment_vars = {
            "name": tk.StringVar(),
            "status": tk.StringVar(value="Stare bună"),
        }
        self.status_var = tk.StringVar(value="Pregătit.")

        self._configure_style()
        self._build_ui()
        self.refresh_objective_choices()

    def _configure_style(self) -> None:
        style = ttk.Style(self)
        available = style.theme_names()
        if "clam" in available:
            style.theme_use("clam")
        style.configure("Title.TLabel", font=("Segoe UI", 17, "bold"))
        style.configure("Hint.TLabel", foreground="#5f6b76")
        style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"))
        style.configure("Treeview", rowheight=28)
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

    def _build_ui(self) -> None:
        header = ttk.Frame(self, padding=(18, 14, 18, 8))
        header.pack(fill="x")
        ttk.Label(header, text=APP_TITLE, style="Title.TLabel").pack(side="left")
        ttk.Button(header, text="Ajutor", command=self.show_help).pack(side="right")

        toolbar = ttk.Frame(self, padding=(18, 4, 18, 10))
        toolbar.pack(fill="x")
        ttk.Label(toolbar, text="Obiectiv salvat:").pack(side="left", padx=(0, 8))
        self.objective_combo = ttk.Combobox(toolbar, state="readonly", width=44)
        self.objective_combo.pack(side="left", fill="x", expand=True, padx=(0, 8))
        self.objective_combo.bind("<<ComboboxSelected>>", self.on_objective_selected)
        ttk.Button(toolbar, text="Obiectiv nou", command=self.new_objective).pack(side="left", padx=4)
        ttk.Button(toolbar, text="Salvează", style="Accent.TButton", command=self.save_objective).pack(
            side="left", padx=4
        )
        ttk.Button(toolbar, text="Șterge", command=self.delete_objective).pack(side="left", padx=4)
        ttk.Button(toolbar, text="Exportă CSV", command=self.export_csv).pack(side="left", padx=(4, 0))

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=18, pady=(0, 8))

        self._build_objective_tab()
        self._build_materials_tab()
        self._build_equipment_tab()
        self._build_consumables_tab()
        self._build_particularities_tab()
        self._build_todo_tab()

        status = ttk.Label(self, textvariable=self.status_var, relief="sunken", anchor="w", padding=(10, 5))
        status.pack(fill="x", side="bottom")

    def _build_objective_tab(self) -> None:
        tab = ttk.Frame(self.notebook, padding=20)
        self.notebook.add(tab, text="Denumire obiectiv")

        ttk.Label(
            tab,
            text="Datele contractului, persoanelor de contact și intervențiilor",
            style="Hint.TLabel",
        ).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 16))

        for column in (1, 3):
            tab.columnconfigure(column, weight=1)

        for index, (name, label) in enumerate(self.OBJECTIVE_FIELDS):
            pair = index % 2
            row = index // 2 + 1
            label_column = pair * 2
            entry_column = label_column + 1
            ttk.Label(tab, text=label).grid(
                row=row, column=label_column, sticky="w", padx=(0 if pair == 0 else 24, 8), pady=8
            )
            entry = ttk.Entry(tab, textvariable=self.objective_vars[name])
            entry.grid(row=row, column=entry_column, sticky="ew", pady=8)
            if name == "company_name":
                self.company_entry = entry

        ttk.Label(tab, text="Zile de intervenție / săptămână").grid(
            row=7, column=0, sticky="nw", pady=8
        )
        weekdays_frame = ttk.Frame(tab)
        weekdays_frame.grid(row=7, column=1, columnspan=3, sticky="w", pady=4)
        for day in WEEKDAYS:
            ttk.Checkbutton(weekdays_frame, text=day, variable=self.weekday_vars[day]).pack(
                side="left", padx=(0, 12), pady=4
            )

        ttk.Label(
            tab,
            text="* Câmp obligatoriu. Numerele pot fi introduse cu virgulă sau punct.",
            style="Hint.TLabel",
        ).grid(row=8, column=0, columnspan=4, sticky="w", pady=(18, 0))

    def _build_materials_tab(self) -> None:
        tab = ttk.Frame(self.notebook, padding=16)
        self.notebook.add(tab, text="Necesar materiale")
        tab.columnconfigure(0, weight=1)
        tab.rowconfigure(2, weight=1)

        form = ttk.LabelFrame(tab, text="Adăugare / modificare material", padding=12)
        form.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        form.columnconfigure(1, weight=1)

        labels = (("name", "Material / produs"), ("needed", "Necesar"), ("stock", "Stoc"))
        for index, (name, label) in enumerate(labels):
            ttk.Label(form, text=label).grid(row=0, column=index * 2, sticky="w", padx=(0 if index == 0 else 14, 6))
            ttk.Entry(form, textvariable=self.material_vars[name], width=22).grid(
                row=0, column=index * 2 + 1, sticky="ew"
            )

        buttons = ttk.Frame(tab)
        buttons.grid(row=1, column=0, sticky="w", pady=(0, 10))
        ttk.Button(buttons, text="Adaugă / actualizează", command=self.add_or_update_material).pack(
            side="left", padx=(0, 6)
        )
        ttk.Button(buttons, text="Golește câmpurile", command=self.clear_material_form).pack(side="left", padx=6)
        ttk.Button(buttons, text="Șterge rândul", command=self.delete_material_row).pack(side="left", padx=6)

        columns = ("material", "needed", "stock", "to_order")
        self.material_tree = ttk.Treeview(tab, columns=columns, show="headings", selectmode="browse")
        self.material_tree.heading("material", text="Material / produs")
        self.material_tree.heading("needed", text="Necesar")
        self.material_tree.heading("stock", text="Stoc")
        self.material_tree.heading("to_order", text="De comandat")
        self.material_tree.column("material", width=410, minwidth=180)
        for column in ("needed", "stock", "to_order"):
            self.material_tree.column(column, width=150, minwidth=90, anchor="center")
        self.material_tree.grid(row=2, column=0, sticky="nsew")
        self.material_tree.bind("<Double-1>", self.edit_material_row)

        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=self.material_tree.yview)
        scrollbar.grid(row=2, column=1, sticky="ns")
        self.material_tree.configure(yscrollcommand=scrollbar.set)
        ttk.Label(
            tab,
            text="„De comandat” se calculează automat: maxim dintre Necesar − Stoc și zero. Dublu clic pentru editare.",
            style="Hint.TLabel",
        ).grid(row=3, column=0, sticky="w", pady=(8, 0))

    def _build_equipment_tab(self) -> None:
        tab = ttk.Frame(self.notebook, padding=16)
        self.notebook.add(tab, text="Necesar echipamente")
        tab.columnconfigure(0, weight=1)
        tab.rowconfigure(2, weight=1)

        form = ttk.LabelFrame(tab, text="Adăugare / modificare echipament", padding=12)
        form.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        form.columnconfigure(1, weight=1)

        ttk.Label(form, text="Echipament").grid(row=0, column=0, sticky="w", padx=(0, 6))
        ttk.Entry(form, textvariable=self.equipment_vars["name"], width=24).grid(
            row=0, column=1, sticky="ew"
        )
        ttk.Label(form, text="Stare").grid(row=0, column=2, sticky="w", padx=(14, 6))
        ttk.Combobox(
            form,
            textvariable=self.equipment_vars["status"],
            values=("Stare bună", "Necesită înlocuire"),
            state="readonly",
            width=20,
        ).grid(row=0, column=3, sticky="w")

        buttons = ttk.Frame(tab)
        buttons.grid(row=1, column=0, sticky="w", pady=(0, 10))
        ttk.Button(buttons, text="Adaugă / actualizează", command=self.add_or_update_equipment).pack(
            side="left", padx=(0, 6)
        )
        ttk.Button(buttons, text="Golește câmpurile", command=self.clear_equipment_form).pack(side="left", padx=6)
        ttk.Button(buttons, text="Șterge rândul", command=self.delete_equipment_row).pack(side="left", padx=6)

        columns = ("equipment", "good", "replace")
        self.equipment_tree = ttk.Treeview(tab, columns=columns, show="headings", selectmode="browse")
        headings = {
            "equipment": "Echipament",
            "good": "Stare bună",
            "replace": "Necesită înlocuire",
        }
        for column, heading in headings.items():
            self.equipment_tree.heading(column, text=heading)
        self.equipment_tree.column("equipment", width=520, minwidth=200)
        self.equipment_tree.column("good", width=220, minwidth=110, anchor="center")
        self.equipment_tree.column("replace", width=260, minwidth=140, anchor="center")
        self.equipment_tree.grid(row=2, column=0, sticky="nsew")
        self.equipment_tree.bind("<Double-1>", self.edit_equipment_row)

        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=self.equipment_tree.yview)
        scrollbar.grid(row=2, column=1, sticky="ns")
        self.equipment_tree.configure(yscrollcommand=scrollbar.set)
        ttk.Label(tab, text="Dublu clic pe un rând pentru editare.", style="Hint.TLabel").grid(
            row=3, column=0, sticky="w", pady=(8, 0)
        )

    def _build_consumables_tab(self) -> None:
        tab = ttk.Frame(self.notebook, padding=16)
        self.notebook.add(tab, text="Necesar consumabile")
        tab.columnconfigure(0, weight=1)
        tab.rowconfigure(2, weight=1)

        form = ttk.LabelFrame(tab, text="Adăugare / modificare consumabil", padding=12)
        form.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        form.columnconfigure(1, weight=1)

        labels = (("name", "Consumabil"), ("needed", "Necesar"), ("stock", "Stoc"))
        for index, (name, label) in enumerate(labels):
            ttk.Label(form, text=label).grid(
                row=0, column=index * 2, sticky="w", padx=(0 if index == 0 else 14, 6)
            )
            ttk.Entry(form, textvariable=self.consumable_vars[name], width=22).grid(
                row=0, column=index * 2 + 1, sticky="ew"
            )

        buttons = ttk.Frame(tab)
        buttons.grid(row=1, column=0, sticky="w", pady=(0, 10))
        ttk.Button(buttons, text="Adaugă / actualizează", command=self.add_or_update_consumable).pack(
            side="left", padx=(0, 6)
        )
        ttk.Button(buttons, text="Golește câmpurile", command=self.clear_consumable_form).pack(
            side="left", padx=6
        )
        ttk.Button(buttons, text="Șterge rândul", command=self.delete_consumable_row).pack(
            side="left", padx=6
        )

        columns = ("consumable", "needed", "stock", "to_order")
        self.consumable_tree = ttk.Treeview(tab, columns=columns, show="headings", selectmode="browse")
        self.consumable_tree.heading("consumable", text="Consumabil")
        self.consumable_tree.heading("needed", text="Necesar")
        self.consumable_tree.heading("stock", text="Stoc")
        self.consumable_tree.heading("to_order", text="De comandat")
        self.consumable_tree.column("consumable", width=410, minwidth=180)
        for column in ("needed", "stock", "to_order"):
            self.consumable_tree.column(column, width=150, minwidth=90, anchor="center")
        self.consumable_tree.grid(row=2, column=0, sticky="nsew")
        self.consumable_tree.bind("<Double-1>", self.edit_consumable_row)

        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=self.consumable_tree.yview)
        scrollbar.grid(row=2, column=1, sticky="ns")
        self.consumable_tree.configure(yscrollcommand=scrollbar.set)
        ttk.Label(
            tab,
            text="„De comandat” se calculează automat: maxim dintre Necesar − Stoc și zero. Dublu clic pentru editare.",
            style="Hint.TLabel",
        ).grid(row=3, column=0, sticky="w", pady=(8, 0))

    def _build_particularities_tab(self) -> None:
        tab = ttk.Frame(self.notebook, padding=16)
        self.notebook.add(tab, text="Particularități")
        tab.columnconfigure(0, weight=1)
        tab.rowconfigure(1, weight=1)

        ttk.Label(
            tab,
            text="Notați aici instrucțiuni speciale, restricții, zone sensibile sau alte observații despre obiectiv.",
            style="Hint.TLabel",
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

        self.particularities_text = tk.Text(
            tab,
            wrap="word",
            undo=True,
            font=("Segoe UI", 11),
            padx=10,
            pady=10,
        )
        self.particularities_text.grid(row=1, column=0, sticky="nsew")
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=self.particularities_text.yview)
        scrollbar.grid(row=1, column=1, sticky="ns")
        self.particularities_text.configure(yscrollcommand=scrollbar.set)

    def _build_todo_tab(self) -> None:
        tab = ttk.Frame(self.notebook, padding=16)
        self.notebook.add(tab, text="ToDoList")
        tab.columnconfigure(0, weight=1)
        tab.rowconfigure(2, weight=1)

        header = ttk.Frame(tab)
        header.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))
        ttk.Label(
            header,
            text="Lista activităților de curățenie pentru obiectivul selectat",
            style="Hint.TLabel",
        ).pack(side="left")
        self.todo_progress_var = tk.StringVar()
        ttk.Label(header, textvariable=self.todo_progress_var).pack(side="right")

        buttons = ttk.Frame(tab)
        buttons.grid(row=1, column=0, sticky="w", pady=(0, 10))
        ttk.Button(buttons, text="Bifează / debifează", command=self.toggle_selected_todo).pack(
            side="left", padx=(0, 6)
        )
        ttk.Button(buttons, text="Toate finalizate", command=lambda: self.set_all_todos(True)).pack(
            side="left", padx=6
        )
        ttk.Button(buttons, text="Resetează lista", command=self.reset_todos).pack(side="left", padx=6)

        columns = ("task", "completed")
        self.todo_tree = ttk.Treeview(tab, columns=columns, show="headings", selectmode="browse")
        self.todo_tree.heading("task", text="Activitate")
        self.todo_tree.heading("completed", text="Stare")
        self.todo_tree.column("task", width=760, minwidth=300)
        self.todo_tree.column("completed", width=220, minwidth=150, anchor="center")
        self.todo_tree.grid(row=2, column=0, sticky="nsew")
        self.todo_tree.tag_configure("completed", foreground="#287a3d")
        self.todo_tree.bind("<Double-1>", self.toggle_selected_todo)
        self.todo_tree.bind("<space>", self.toggle_selected_todo)

        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=self.todo_tree.yview)
        scrollbar.grid(row=2, column=1, sticky="ns")
        self.todo_tree.configure(yscrollcommand=scrollbar.set)
        ttk.Label(
            tab,
            text="Selectați o activitate și apăsați butonul, tasta Spațiu sau dublu clic. Apăsați «Salvează» pentru păstrare.",
            style="Hint.TLabel",
        ).grid(row=3, column=0, sticky="w", pady=(8, 0))
        self._populate_todo_tree()

    def refresh_objective_choices(self, select_id: int | None = None) -> None:
        rows = self.db.list_objectives()
        self.objective_choices = []
        labels: list[str] = []
        for row in rows:
            suffix = f" — {row['address']}" if row["address"] else ""
            label = f"{row['company_name']}{suffix}"
            self.objective_choices.append((int(row["id"]), label))
            labels.append(label)
        self.objective_combo["values"] = labels

        if select_id is not None:
            for index, (objective_id, _) in enumerate(self.objective_choices):
                if objective_id == select_id:
                    self.objective_combo.current(index)
                    break
        elif not labels:
            self.objective_combo.set("")

    def on_objective_selected(self, _event: tk.Event[tk.Misc] | None = None) -> None:
        index = self.objective_combo.current()
        if index < 0:
            return
        self.load_objective(self.objective_choices[index][0])

    def load_objective(self, objective_id: int) -> None:
        row = self.db.get_objective(objective_id)
        if row is None:
            messagebox.showerror("Eroare", "Obiectivul nu mai există.")
            self.refresh_objective_choices()
            return
        self.current_objective_id = objective_id

        for name, _ in self.OBJECTIVE_FIELDS:
            value = row[name]
            if name in {
                "location_area",
                "contract_value",
                "cleaning_agent_salary",
                "intervention_duration_hours",
            }:
                self.objective_vars[name].set(format_number(value))
            else:
                self.objective_vars[name].set(value or "")

        selected_weekdays = {
            day.strip() for day in str(row["intervention_weekdays"] or "").split(",") if day.strip()
        }
        for day, variable in self.weekday_vars.items():
            variable.set(day in selected_weekdays)

        self._clear_tree(self.material_tree)
        for material in self.db.get_materials(objective_id):
            self.material_tree.insert(
                "",
                "end",
                values=(
                    material["material_name"],
                    format_number(material["needed"]),
                    format_number(material["stock"]),
                    format_number(material["to_order"]),
                ),
            )

        self._clear_tree(self.equipment_tree)
        for item in self.db.get_equipment(objective_id):
            self.equipment_tree.insert(
                "",
                "end",
                values=(
                    item["equipment_name"],
                    "Da" if item["good_condition"] else "Nu",
                    "Da" if item["needs_replacement"] else "Nu",
                ),
            )

        self._clear_tree(self.consumable_tree)
        for consumable in self.db.get_consumables(objective_id):
            self.consumable_tree.insert(
                "",
                "end",
                values=(
                    consumable["consumable_name"],
                    format_number(consumable["needed"]),
                    format_number(consumable["stock"]),
                    format_number(consumable["to_order"]),
                ),
            )

        self.particularities_text.delete("1.0", "end")
        self.particularities_text.insert("1.0", self.db.get_particularities(objective_id))
        todo_rows = self.db.get_todos(objective_id)
        if todo_rows:
            self._populate_todo_tree(
                [(str(todo["task_name"]), bool(todo["completed"])) for todo in todo_rows]
            )
        else:
            self._populate_todo_tree()
        self.clear_material_form()
        self.clear_equipment_form()
        self.clear_consumable_form()
        self.status_var.set(f"Obiectiv încărcat: {row['company_name']}")

    def new_objective(self) -> None:
        self.current_objective_id = None
        self.objective_combo.set("")
        for variable in self.objective_vars.values():
            variable.set("")
        for variable in self.weekday_vars.values():
            variable.set(False)
        self._clear_tree(self.material_tree)
        self._clear_tree(self.equipment_tree)
        self._clear_tree(self.consumable_tree)
        self.particularities_text.delete("1.0", "end")
        self._populate_todo_tree()
        self.clear_material_form()
        self.clear_equipment_form()
        self.clear_consumable_form()
        self.notebook.select(0)
        self.company_entry.focus_set()
        self.status_var.set("Obiectiv nou. Completați datele și apăsați «Salvează».")

    def _validated_objective(self) -> dict[str, object]:
        company = self.objective_vars["company_name"].get().strip()
        if not company:
            raise ValueError("Denumirea firmei este obligatorie.")

        date_value = self.objective_vars["contract_start_date"].get().strip()
        if date_value:
            try:
                datetime.strptime(date_value, "%Y-%m-%d")
            except ValueError as exc:
                raise ValueError("Data începerii contractului trebuie scrisă AAAA-LL-ZZ.") from exc

        return {
            "company_name": company,
            "address": self.objective_vars["address"].get().strip(),
            "location_area": parse_number(self.objective_vars["location_area"].get(), "Suprafață locație"),
            "contract_start_date": date_value,
            "contract_value": parse_number(self.objective_vars["contract_value"].get(), "Valoare contract"),
            "contact_person": self.objective_vars["contact_person"].get().strip(),
            "contact_details": self.objective_vars["contact_details"].get().strip(),
            "cleaning_agent_name": self.objective_vars["cleaning_agent_name"].get().strip(),
            "cleaning_agent_contact": self.objective_vars["cleaning_agent_contact"].get().strip(),
            "cleaning_agent_salary": parse_number(
                self.objective_vars["cleaning_agent_salary"].get(), "Salariu agent curățenie"
            ),
            "intervention_weekdays": ",".join(
                day for day in WEEKDAYS if self.weekday_vars[day].get()
            ),
            "intervention_duration_hours": parse_number(
                self.objective_vars["intervention_duration_hours"].get(), "Durata intervenției"
            ),
            "updated_at": datetime.now().isoformat(timespec="seconds"),
        }

    def save_objective(self) -> None:
        try:
            objective = self._validated_objective()
            materials = self._materials_from_tree()
            equipment = self._equipment_from_tree()
            consumables = self._consumables_from_tree()
            particularities = self.particularities_text.get("1.0", "end-1c").strip()
            todos = self._todos_from_tree()
            self.current_objective_id = self.db.save_all(
                self.current_objective_id,
                objective,
                materials,
                equipment,
                consumables,
                particularities,
                todos,
            )
        except (ValueError, psycopg2.Error) as exc:
            messagebox.showerror("Date nevalide", str(exc))
            return

        self.refresh_objective_choices(self.current_objective_id)
        self.status_var.set(f"Date salvate pentru {objective['company_name']}.")
        messagebox.showinfo(
            "Salvare",
            "Obiectivul și toate datele sale, inclusiv ToDoList-ul, au fost salvate.",
        )

    def delete_objective(self) -> None:
        if self.current_objective_id is None:
            messagebox.showwarning("Ștergere", "Selectați mai întâi un obiectiv salvat.")
            return
        company = self.objective_vars["company_name"].get().strip()
        confirmed = messagebox.askyesno(
            "Confirmare ștergere",
            f"Ștergeți obiectivul «{company}» împreună cu materialele și echipamentele sale?",
        )
        if not confirmed:
            return
        try:
            self.db.delete_objective(self.current_objective_id)
        except psycopg2.Error as exc:
            messagebox.showerror("Eroare", f"Obiectivul nu a putut fi șters:\n{exc}")
            return
        self.new_objective()
        self.refresh_objective_choices()
        self.status_var.set(f"Obiectiv șters: {company}")

    def add_or_update_material(self) -> None:
        name = self.material_vars["name"].get().strip()
        if not name:
            messagebox.showwarning("Material", "Introduceți denumirea materialului sau produsului.")
            return
        try:
            needed = parse_number(self.material_vars["needed"].get(), "Necesar")
            stock = parse_number(self.material_vars["stock"].get(), "Stoc")
        except ValueError as exc:
            messagebox.showerror("Date nevalide", str(exc))
            return
        needed = float(needed or 0)
        stock = float(stock or 0)
        to_order = max(needed - stock, 0)
        values = (name, format_number(needed), format_number(stock), format_number(to_order))
        selection = self.material_tree.selection()
        if selection:
            self.material_tree.item(selection[0], values=values)
        else:
            self.material_tree.insert("", "end", values=values)
        self.clear_material_form()
        self.status_var.set("Rândul de material a fost actualizat. Salvați obiectivul pentru păstrare.")

    def edit_material_row(self, _event: tk.Event[tk.Misc] | None = None) -> None:
        selection = self.material_tree.selection()
        if not selection:
            return
        values = self.material_tree.item(selection[0], "values")
        self.material_vars["name"].set(values[0])
        self.material_vars["needed"].set(values[1])
        self.material_vars["stock"].set(values[2])

    def clear_material_form(self) -> None:
        for variable in self.material_vars.values():
            variable.set("")
        for item in self.material_tree.selection():
            self.material_tree.selection_remove(item)

    def delete_material_row(self) -> None:
        selection = self.material_tree.selection()
        if not selection:
            messagebox.showwarning("Material", "Selectați rândul pe care doriți să îl ștergeți.")
            return
        self.material_tree.delete(selection[0])
        self.clear_material_form()
        self.status_var.set("Rândul a fost șters. Salvați obiectivul pentru păstrare.")

    def add_or_update_consumable(self) -> None:
        name = self.consumable_vars["name"].get().strip()
        if not name:
            messagebox.showwarning("Consumabil", "Introduceți denumirea consumabilului.")
            return
        try:
            needed = parse_number(self.consumable_vars["needed"].get(), "Necesar consumabile")
            stock = parse_number(self.consumable_vars["stock"].get(), "Stoc consumabile")
        except ValueError as exc:
            messagebox.showerror("Date nevalide", str(exc))
            return
        needed = float(needed or 0)
        stock = float(stock or 0)
        to_order = max(needed - stock, 0)
        values = (name, format_number(needed), format_number(stock), format_number(to_order))
        selection = self.consumable_tree.selection()
        if selection:
            self.consumable_tree.item(selection[0], values=values)
        else:
            self.consumable_tree.insert("", "end", values=values)
        self.clear_consumable_form()
        self.status_var.set("Rândul de consumabil a fost actualizat. Salvați obiectivul pentru păstrare.")

    def edit_consumable_row(self, _event: tk.Event[tk.Misc] | None = None) -> None:
        selection = self.consumable_tree.selection()
        if not selection:
            return
        values = self.consumable_tree.item(selection[0], "values")
        self.consumable_vars["name"].set(values[0])
        self.consumable_vars["needed"].set(values[1])
        self.consumable_vars["stock"].set(values[2])

    def clear_consumable_form(self) -> None:
        for variable in self.consumable_vars.values():
            variable.set("")
        for item in self.consumable_tree.selection():
            self.consumable_tree.selection_remove(item)

    def delete_consumable_row(self) -> None:
        selection = self.consumable_tree.selection()
        if not selection:
            messagebox.showwarning("Consumabil", "Selectați rândul pe care doriți să îl ștergeți.")
            return
        self.consumable_tree.delete(selection[0])
        self.clear_consumable_form()
        self.status_var.set("Rândul a fost șters. Salvați obiectivul pentru păstrare.")

    def add_or_update_equipment(self) -> None:
        name = self.equipment_vars["name"].get().strip()
        if not name:
            messagebox.showwarning("Echipament", "Introduceți denumirea echipamentului.")
            return
        status = self.equipment_vars["status"].get()
        good = status == "Stare bună"
        values = (
            name,
            "Da" if good else "Nu",
            "Nu" if good else "Da",
        )
        selection = self.equipment_tree.selection()
        if selection:
            self.equipment_tree.item(selection[0], values=values)
        else:
            self.equipment_tree.insert("", "end", values=values)
        self.clear_equipment_form()
        self.status_var.set("Rândul de echipament a fost actualizat. Salvați obiectivul pentru păstrare.")

    def edit_equipment_row(self, _event: tk.Event[tk.Misc] | None = None) -> None:
        selection = self.equipment_tree.selection()
        if not selection:
            return
        values = self.equipment_tree.item(selection[0], "values")
        self.equipment_vars["name"].set(values[0])
        self.equipment_vars["status"].set("Stare bună" if values[1] == "Da" else "Necesită înlocuire")

    def clear_equipment_form(self) -> None:
        self.equipment_vars["name"].set("")
        self.equipment_vars["status"].set("Stare bună")
        for item in self.equipment_tree.selection():
            self.equipment_tree.selection_remove(item)

    def delete_equipment_row(self) -> None:
        selection = self.equipment_tree.selection()
        if not selection:
            messagebox.showwarning("Echipament", "Selectați rândul pe care doriți să îl ștergeți.")
            return
        self.equipment_tree.delete(selection[0])
        self.clear_equipment_form()
        self.status_var.set("Rândul a fost șters. Salvați obiectivul pentru păstrare.")

    def _materials_from_tree(self) -> list[tuple[str, float, float, float]]:
        result: list[tuple[str, float, float, float]] = []
        for item_id in self.material_tree.get_children():
            values = self.material_tree.item(item_id, "values")
            result.append((values[0], float(values[1]), float(values[2]), float(values[3])))
        return result

    def _equipment_from_tree(self) -> list[tuple[str, bool, bool]]:
        result: list[tuple[str, bool, bool]] = []
        for item_id in self.equipment_tree.get_children():
            values = self.equipment_tree.item(item_id, "values")
            result.append((values[0], values[1] == "Da", values[2] == "Da"))
        return result

    def _consumables_from_tree(self) -> list[tuple[str, float, float, float]]:
        result: list[tuple[str, float, float, float]] = []
        for item_id in self.consumable_tree.get_children():
            values = self.consumable_tree.item(item_id, "values")
            result.append((values[0], float(values[1]), float(values[2]), float(values[3])))
        return result

    def _populate_todo_tree(self, tasks: list[tuple[str, bool]] | None = None) -> None:
        self._clear_tree(self.todo_tree)
        task_rows = tasks if tasks is not None else [(task, False) for task in DEFAULT_TODO_TASKS]
        for task_name, completed in task_rows:
            self.todo_tree.insert(
                "",
                "end",
                values=(task_name, "☑ Finalizat" if completed else "☐ De făcut"),
                tags=("completed",) if completed else (),
            )
        self._update_todo_progress()

    def toggle_selected_todo(self, _event: tk.Event[tk.Misc] | None = None) -> None:
        selection = self.todo_tree.selection()
        if not selection:
            messagebox.showwarning("ToDoList", "Selectați mai întâi o activitate.")
            return
        item_id = selection[0]
        values = self.todo_tree.item(item_id, "values")
        completed = str(values[1]).startswith("☑")
        new_completed = not completed
        self.todo_tree.item(
            item_id,
            values=(values[0], "☑ Finalizat" if new_completed else "☐ De făcut"),
            tags=("completed",) if new_completed else (),
        )
        self._update_todo_progress()
        self.status_var.set("ToDoList actualizat. Salvați obiectivul pentru păstrare.")

    def set_all_todos(self, completed: bool) -> None:
        for item_id in self.todo_tree.get_children():
            values = self.todo_tree.item(item_id, "values")
            self.todo_tree.item(
                item_id,
                values=(values[0], "☑ Finalizat" if completed else "☐ De făcut"),
                tags=("completed",) if completed else (),
            )
        self._update_todo_progress()
        self.status_var.set("ToDoList actualizat. Salvați obiectivul pentru păstrare.")

    def reset_todos(self) -> None:
        if messagebox.askyesno("Resetare ToDoList", "Debifați toate activitățile din listă?"):
            self.set_all_todos(False)

    def _update_todo_progress(self) -> None:
        items = self.todo_tree.get_children()
        completed = sum(
            str(self.todo_tree.item(item_id, "values")[1]).startswith("☑") for item_id in items
        )
        self.todo_progress_var.set(f"Finalizate: {completed} / {len(items)}")

    def _todos_from_tree(self) -> list[tuple[str, bool]]:
        result: list[tuple[str, bool]] = []
        for item_id in self.todo_tree.get_children():
            values = self.todo_tree.item(item_id, "values")
            result.append((values[0], str(values[1]).startswith("☑")))
        return result

    def export_csv(self) -> None:
        if self.current_objective_id is None:
            messagebox.showwarning("Export", "Salvați sau selectați mai întâi un obiectiv.")
            return
        default_name = self._safe_filename(self.objective_vars["company_name"].get()) + ".csv"
        path = filedialog.asksaveasfilename(
            title="Exportă obiectivul",
            defaultextension=".csv",
            initialfile=default_name,
            filetypes=(("Fișiere CSV", "*.csv"), ("Toate fișierele", "*.*")),
        )
        if not path:
            return
        try:
            with open(path, "w", newline="", encoding="utf-8-sig") as handle:
                writer = csv.writer(handle, delimiter=";")
                writer.writerow(("OBIECTIV", "VALOARE"))
                for name, label in self.OBJECTIVE_FIELDS:
                    writer.writerow((label.replace(" *", ""), self.objective_vars[name].get().strip()))
                writer.writerow(
                    (
                        "Zile de intervenție / săptămână",
                        ", ".join(day for day in WEEKDAYS if self.weekday_vars[day].get()),
                    )
                )
                writer.writerow(())
                writer.writerow(("MATERIALE", "NECESAR", "STOC", "DE COMANDAT"))
                for row in self._materials_from_tree():
                    writer.writerow(row)
                writer.writerow(())
                writer.writerow(("ECHIPAMENTE", "STARE BUNĂ", "NECESITĂ ÎNLOCUIRE"))
                for row in self._equipment_from_tree():
                    writer.writerow((row[0], "Da" if row[1] else "Nu", "Da" if row[2] else "Nu"))
                writer.writerow(())
                writer.writerow(("CONSUMABILE", "NECESAR", "STOC", "DE COMANDAT"))
                for row in self._consumables_from_tree():
                    writer.writerow(row)
                writer.writerow(())
                writer.writerow(("PARTICULARITĂȚI",))
                writer.writerow((self.particularities_text.get("1.0", "end-1c").strip(),))
                writer.writerow(())
                writer.writerow(("TODOLIST", "FINALIZAT"))
                for task_name, completed in self._todos_from_tree():
                    writer.writerow((task_name, "Da" if completed else "Nu"))
        except OSError as exc:
            messagebox.showerror("Export", f"Fișierul nu a putut fi scris:\n{exc}")
            return
        self.status_var.set(f"Export realizat: {path}")
        messagebox.showinfo("Export", "Fișierul CSV a fost creat.")

    @staticmethod
    def _safe_filename(value: str) -> str:
        cleaned = "".join(character if character.isalnum() or character in "-_" else "_" for character in value)
        return cleaned.strip("_") or "obiectiv_curatenie"

    @staticmethod
    def _clear_tree(tree: ttk.Treeview) -> None:
        children = tree.get_children()
        if children:
            tree.delete(*children)

    def show_help(self) -> None:
        messagebox.showinfo(
            "Ajutor",
            "1. Apăsați «Obiectiv nou» și completați datele firmei.\n"
            "2. Adăugați materialele, echipamentele și consumabilele în taburile lor.\n"
            "3. Completați instrucțiunile speciale în tabul «Particularități».\n"
            "4. Bifați activitățile efectuate în tabul «ToDoList».\n"
            "5. Apăsați «Salvează» pentru a păstra toate datele.\n"
            "6. Selectați ulterior obiectivul din lista de sus pentru modificare.\n\n"
            "Cantitatea «De comandat» este calculată automat. Datele sunt păstrate în PostgreSQL.",
        )

    def on_close(self) -> None:
        self.db.close()
        self.destroy()


def main() -> None:
    try:
        database = Database()
    except psycopg2.Error as exc:
        error_window = tk.Tk()
        error_window.withdraw()
        messagebox.showerror(
            "Conexiune PostgreSQL",
            "Conexiunea la PostgreSQL nu a putut fi realizată.\n\n"
            "Configurați DATABASE_URL sau variabilele PGHOST, PGPORT, PGDATABASE, "
            "PGUSER și PGPASSWORD.\n\n"
            f"Detalii: {str(exc).strip()}",
        )
        error_window.destroy()
        return

    try:
        app = CleaningManagementApp(database)
    except Exception:
        database.close()
        raise
    app.mainloop()


if __name__ == "__main__":
    main()
