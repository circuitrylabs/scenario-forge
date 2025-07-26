"""Minimal SQLite datastore for scenarios."""

import sqlite3
from pathlib import Path
from typing import Optional, List

from scenario_forge.core import Scenario


class ScenarioStore:
    """Minimal scenario storage."""

    def __init__(self, db_path: Optional[Path] = None):
        """Initialize the datastore."""
        if db_path is None:
            db_dir = Path.home() / ".scenario-forge"
            db_dir.mkdir(exist_ok=True)
            db_path = db_dir / "scenarios.db"

        self.db_path = db_path
        self._init_db()

    def _init_db(self) -> None:
        """Create the scenarios table."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS scenarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prompt TEXT NOT NULL,
                    evaluation_target TEXT NOT NULL,
                    success_criteria TEXT NOT NULL,
                    backend TEXT,
                    model TEXT,
                    temperature REAL
                )
            """)
            conn.commit()

    def save_scenario(
        self,
        scenario: Scenario,
        backend: Optional[str] = None,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
    ) -> int:
        """Save a scenario and return its ID."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                """
                INSERT INTO scenarios (
                    prompt, evaluation_target, success_criteria,
                    backend, model, temperature
                ) VALUES (?, ?, ?, ?, ?, ?)
            """,
                (
                    scenario.prompt,
                    scenario.evaluation_target,
                    scenario.success_criteria,
                    backend,
                    model,
                    temperature,
                ),
            )
            return cursor.lastrowid

    def get_scenario(self, scenario_id: int) -> Optional[Scenario]:
        """Get a scenario by ID."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                "SELECT * FROM scenarios WHERE id = ?", (scenario_id,)
            ).fetchone()

            if row:
                return Scenario(
                    prompt=row["prompt"],
                    evaluation_target=row["evaluation_target"],
                    success_criteria=row["success_criteria"],
                )
            return None

    def list_all_scenarios(self) -> List[Scenario]:
        """List all scenarios."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute("SELECT * FROM scenarios ORDER BY id DESC").fetchall()

            return [
                Scenario(
                    prompt=row["prompt"],
                    evaluation_target=row["evaluation_target"],
                    success_criteria=row["success_criteria"],
                )
                for row in rows
            ]
