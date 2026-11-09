import tomli
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        
        parsed_toml = tomli.loads(content)

        project_data = parsed_toml.get("project", {})

        name = project_data.get("name", "Test name")
        description = project_data.get("description", "Test description")
        
        license_data = project_data.get("license", "-")
        if isinstance(license_data, dict):
            license_name = license_data.get("text", "-")
        else:
            license_name = license_data

        authors = []
        for author in project_data.get("authors", []):
            if isinstance(author, dict) and "name" in author:
                authors.append(author["name"])
            else:
                authors.append(str(author))

        dependencies = project_data.get("dependencies", [])

        dev_dependencies = parsed_toml.get("dependency-groups", {}).get("dev", [])
        if not dev_dependencies:
            dev_dependencies = parsed_toml.get("tool", {}).get("uv", {}).get("dev-dependencies", [])

        return Project(name, description, license_name, authors, dependencies, dev_dependencies)
