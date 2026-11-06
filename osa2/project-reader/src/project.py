class Project:
    def __init__(self, name, description, authors, licence, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.authors = authors
        self.licence = license
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_items(self, items):
         return "\n".join(f"- {item}" for item in items) if len(items) > 0 else "-"

    def __str__(self):
        authors = self._stringify_items([author["name"] for author in self.authors])
        dependencies = self._stringify_items(self.dependencies)
        dev_dependencies = self._stringify_items(self.dev_dependencies)
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicence: {self.licence}"
            f"\n\nAuthors:\n{authors}"
            f"\n\nDependencies:\n{dependencies}"
            f"\n\nDevelopment dependencies:\n{dev_dependencies}"
        )
