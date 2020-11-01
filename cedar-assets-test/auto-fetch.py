import requests
import json
import os


FOLDER_URL = "https://resource.metadatacenter.org/folders/https%3A%2F%2Frepo.metadatacenter.org%2Ffolders%2Fdaf80275-83d3-4034-bfbf-2c62ff39902b/"
CEDAR_CMD = "contents-extract?version=all&publication_status=all&sort=name"
FOLDER_CMD = "contents?version=latest&publication_status=all&sort=name"
ELEMENT_BASE_URL = "https://resource.metadatacenter.org/template-elements/https%3A%2F%2Frepo.metadatacenter.org%2Ftemplate-elements%2F"

headers = {
    "Accept": "application/json",
    "Authorization": "apiKey " + os.environ["CEDAR_API"],
}


response = requests.get(FOLDER_URL + FOLDER_CMD, headers=headers).json()


for artifact in response["resources"]:
    if artifact["resourceType"] == "element":
        cmd = ELEMENT_BASE_URL + artifact["@id"].replace(
            "https://repo.metadatacenter.org/template-elements/", ""
        )
        element_json = requests.get(cmd, headers=headers).json()
        path = "./cedar-assets-test/Elements/" + artifact["schema:name"] + ".json"

        with open(path, "w") as json_file:
            json.dump(element_json, json_file, indent=4)
