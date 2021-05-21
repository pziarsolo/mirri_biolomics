def retrieve_strain_by_accession_number(client, accession_number):
    query = {"Query": [{"Index": 0,
                        "FieldName": "Collection accession number",
                        "Operation": "TextExactMatch",
                        "Value": accession_number}],
             "Expression": "Q0",
             "DisplayStart": 0,
             "DisplayLength": 10}

    result = client.search('strain', query=query)

    total = result["total"]
    if total == 0:
        return None
    elif total == 1:
        return result["records"][0]
    else:
        msg = "More than one entries for {accession_number} in database"
        raise ValueError(msg)

def create_or_update_strain(strain, force_update=True):