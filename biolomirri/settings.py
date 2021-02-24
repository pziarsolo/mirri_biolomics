

MIRRI_FIELDS = [
    {
        "attribute": "id",
        "label": "Accession number",
        "mandatory": True,
        "biolomics": {"field": "Collection accession number", "type": "E"},
    },
    {
        "attribute": "restriction_on_use",
        "label": "Restrictions on use",
        "mandatory": True,
        "biolomics": {"field": "Restrictions on use", "type": "T"},
    },
    {
        "attribute": "nagoya_protocol",
        "label": "Nagoya protocol restrictions and compliance conditions",
        "mandatory": True,
        "biolomics": {"field": "Nagoya protocol restrictions and compliance conditions", "type": "T"},
    },
    {
        "attribute": "abs_related_files",
        "label": "ABS related files",
        "mandatory": False,
        "biolomics": {"field": "ABS files URL", "type": "U"},
    },
    {
        "attribute": "mta_file",
        "label": "MTA file",
        "mandatory": False,
        "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "other_numbers",
        "label": "Other culture collection numbers",
        "mandatory": False,
    },
    {
        "attribute": "is_from_registered_collection",
        "label": "Strain from a registered collection",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "risk_group",
        "label": "Risk Group",
        "mandatory": True,
        "biolomics": {"field": "Risk group", "type": "T"},
    },
    {
        "attribute": "dual_use",
        "label": "Dual use",
        "mandatory": False,
        "type": int,
        # "biolomics": {"field": "Risk group", "type": "T"},
    },
    {
        "attribute": "is_subject_to_quarantine",
        "label": "Quarantine in Europe",
        "mandatory": False,
        "type": int,
    },
    {
        "attribute": "taxonomy.organism_type",
        "label": "Organism type",
        "mandatory": True,
        "type": str,
        "biolomics": {"field": "Organism type", "type": "C"},
    },
    {
        "attribute": "taxonomy.taxon_name",
        "label": "Taxon name",
        "mandatory": True,
        "type": str,
        # "biolomics": {"field": "Organism type", "type": "C"},
    },
    {
        "attribute": "taxonomy.infrasubspecific_name",
        "label": "Infrasubspecific names",
        "mandatory": False,
        "type": str,
    },
    {
        "attribute": "taxonomy.comments",
        "label": "Comment on taxonomy",
        "mandatory": False,
        "type": str,
    },
    {
        "attribute": "taxonomy.interspecific_hybrid",
        "label": "Interspecific hybrid",
        "mandatory": False,
        "type": int,
    },
    {"attribute": "status", "label": "Status", "mandatory": False, "type": str},
    {
        "attribute": "history",
        "label": "History of deposit",
        "mandatory": False,
        "type": str,
    },
    {
        "attribute": "deposit.who",
        "label": "Depositor",
        "mandatory": False,
        "type": str,
        "biolomics": {"field": "Depositor", "type": "E"},
    },
    {
        "attribute": "deposit.date",
        "label": "Date of deposit",
        "mandatory": False,
        "type": "datetime",
    },
    {
        "attribute": "catalog_inclusion_date",
        "label": "Date of inclusion in the catalogue",
        "mandatory": False,
        "type": "datetime",
        "biolomics": {"field": "Date of inclusion in the catalogue", "type": "H"},
    },
    {
        "attribute": "collect.who",
        "label": "Collected by",
        "mandatory": False,
        "type": str,
        "biolomics": {"field": "Collector", "type": "E"},
    },
    {
        "attribute": "collect.date",
        "label": "Date of collection",
        "mandatory": False,
        "type": "datetime",
        "biolomics": {"field": "Collection date", "type": "H"},
    },
    {
        "attribute": "isolation.who",
        "label": "Isolated by",
        "mandatory": False,
        "type": str,
        "biolomics": {"field": "Isolator", "type": "E"},
    },
    {
        "attribute": "isolation.date",
        "label": "Date of isolation",
        "mandatory": False,
        "type": "datetime",
        "biolomics": {"field": "Isolation date", "type": "H"},
    },
    {
        "attribute": "isolation.substrate_host_of_isolation",
        "label": "Substrate/host of isolation",
        "mandatory": False,
        "type": str,
    },
    {
        "attribute": "growth.tested_temp_range",
        "label": "Tested temperature growth range",
        "mandatory": False,
        "type": float,
    },
    {
        "attribute": "growth.recommended_temp",
        "label": "Recommended growth temperature",
        "mandatory": True,
        "type": float,
        "biolomics": {"field": "Recommended growth temperature", "type": "S"},
    },
    {
        "attribute": "growth.recommended_medium",
        "label": "Recommended medium for growth",
        "mandatory": True,
        "type": str,
        "biolomics": {"field": "Recommended growth medium", "type": "Rlink"},
    },
    {
        "attribute": "form_of_supply",
        "label": "Form of supply",
        "mandatory": True,
        "type": str,
        "biolomics": {"field": "Form", "type": "C"},
    },
    {
        "attribute": "other_denominations",
        "label": "Other denomination",
        "mandatory": False,
        "type": str,
    },
    {
        "attribute": "collect.location.coords",
        "label": "Coordinates of geographic origin",
        "mandatory": False,
        "type": float,
    },
    {
        "attribute": "collect.location.altidude",
        "label": "Altitude of geographic origin",
        "mandatory": False,
        "type": float,
        "biolomics": {"field": "Altitude of geographic origin", "type": "D"},
    },
    {
        "attribute": "collect.location",
        "label": "Geographic origin",
        "mandatory": True,
        "type": str,
    },
    {
        "attribute": "collect.habitat",
        "label": "Isolation habitat",
        "mandatory": False,
        "type": str,
    },
    {
        "attribute": "collect.habitat_ontobiotope",
        "label": "Ontobiotope term for the isolation habitat",
        "mandatory": False,
        "type": str,
    },
    {"attribute": "genetics.gmo", "label": "GMO", "mandatory": False, "type": int},
    {
        "attribute": "genetics.gmo_construction",
        "label": "GMO construction information",
        "mandatory": False,
        "type": str,
    },
    {
        "attribute": "genetics.mutant_info",
        "label": "Mutant information",
        "mandatory": False,
        "type": str,
    },
    {
        "attribute": "genetics.genotype",
        "label": "Genotype",
        "mandatory": False,
        "type": str,
    },
    {
        "attribute": "genetics.sexual_state",
        "label": "Sexual state",
        "mandatory": False,
        "type": str,
    },
    {
        "attribute": "genetics.ploidy",
        "label": "Ploidy",
        "mandatory": False,
        "type": int,
    },
    {
        "attribute": "genetics.plasmids",
        "label": "Plasmids",
        "mandatory": False,
        "type": str,
    },
    {
        "attribute": "genetics.plasmid_collections_fields",
        "label": "Plasmids collections fields",
        "mandatory": False,
        "type": str,
    },
    {
        "attribute": "publications",
        "label": "Literature",
        "mandatory": False,
        "type": float,
    },
    {
        "attribute": "plant_pathogenicity_code",
        "label": "Plant pathogenicity code",
        "mandatory": False,
        "type": str,
    },
    {
        "attribute": "pathogenity",
        "label": "Pathogenicity",
        "mandatory": False,
        "type": str,
    },
    {
        "attribute": "enzyme_production",
        "label": "Enzyme production",
        "mandatory": False,
        "type": str,
    },
    {
        "attribute": "production_of_metabolites",
        "label": "Production of metabolites",
        "mandatory": False,
        "type": str,
    },
    {
        "attribute": "applications",
        "label": "Applications",
        "mandatory": False,
        "type": str,
        "biolomics": {"field": "Applications", "type": "E"},
    },
    {"attribute": "remarks", "label": "Remarks", "mandatory": False, "type": str},
    {
        "attribute": "literature_linked_to_the_sequence_genome",
        "label": "Literature linked to the sequence/genome",
        "mandatory": False,
        "type": float,
    },
]


# nagoya
NAGOYA_NO_APPLIES = "nagoya_does_not_apply"
NAGOYA_APPLIES = "nagoya_does_apply"
NAGOYA_NO_CLEAR_APPLIES = "nagoya_no_clear"

ALLOWED_NAGOYA_OPTIONS = [NAGOYA_NO_APPLIES,
                          NAGOYA_APPLIES, NAGOYA_NO_CLEAR_APPLIES]

# Use restriction
NO_RESTRICTION = "no_restriction"
ONLY_RESEARCH = "only_research"
COMMERCIAL_USE_WITH_AGREEMENT = "commercial_use_with_agreement"

ALLOWED_RESTRICTION_USE_OPTIONS = [
    NO_RESTRICTION,
    ONLY_RESEARCH,
    COMMERCIAL_USE_WITH_AGREEMENT,
]
