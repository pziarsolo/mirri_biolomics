

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
        # "biolomics": {"field": "MTA files URL", "type": "U"},
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
        # "biolomics": {"field": "Risk group", "type": "T"},
    },
    {
        "attribute": "is_subject_to_quarantine",
        "label": "Quarantine in Europe",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "taxonomy.organism_type",
        "label": "Organism type",
        "mandatory": True,
        "biolomics": {"field": "Organism type", "type": "C"},
    },
    {
        "attribute": "taxonomy.taxon_name",
        "label": "Taxon name",
        "mandatory": True,
        # "biolomics": {"field": "Organism type", "type": "C"},
    },
    {
        "attribute": "taxonomy.infrasubspecific_name",
        "label": "Infrasubspecific names",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "taxonomy.comments",
        "label": "Comment on taxonomy",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "taxonomy.interspecific_hybrid",
        "label": "Interspecific hybrid",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "status", "label": "Status", "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "history",
        "label": "History of deposit",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "deposit.who",
        "label": "Depositor",
        "mandatory": False,
        "biolomics": {"field": "Depositor", "type": "E"},
    },
    {
        "attribute": "deposit.date",
        "label": "Date of deposit",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "catalog_inclusion_date",
        "label": "Date of inclusion in the catalogue",
        "mandatory": False,
        "biolomics": {"field": "Date of inclusion in the catalogue", "type": "H"},
    },
    {
        "attribute": "collect.who",
        "label": "Collected by",
        "mandatory": False,
        "biolomics": {"field": "Collector", "type": "E"},
    },
    {
        "attribute": "collect.date",
        "label": "Date of collection",
        "mandatory": False,
        "biolomics": {"field": "Collection date", "type": "H"},
    },
    {
        "attribute": "isolation.who",
        "label": "Isolated by",
        "mandatory": False,
        "biolomics": {"field": "Isolator", "type": "E"},
    },
    {
        "attribute": "isolation.date",
        "label": "Date of isolation",
        "mandatory": False,
        "biolomics": {"field": "Isolation date", "type": "H"},
    },
    {
        "attribute": "isolation.substrate_host_of_isolation",
        "label": "Substrate/host of isolation",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "growth.tested_temp_range",
        "label": "Tested temperature growth range",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "growth.recommended_temp",
        "label": "Recommended growth temperature",
        "mandatory": True,
        "biolomics": {"field": "Recommended growth temperature", "type": "S"},
    },
    {
        "attribute": "growth.recommended_media",
        "label": "Recommended medium for growth",
        "mandatory": True,
        "biolomics": {"field": "Recommended growth medium", "type": "Rlink"},
    },
    {
        "attribute": "form_of_supply",
        "label": "Form of supply",
        "mandatory": True,
        "biolomics": {"field": "Form", "type": "C"},
    },
    {
        "attribute": "other_denominations",
        "label": "Other denomination",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "collect.location.coords",
        "label": "Coordinates of geographic origin",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "collect.location.altitude",
        "label": "Altitude of geographic origin",
        "mandatory": False,
        "biolomics": {"field": "Altitude of geographic origin", "type": "D"},
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "collect.location",
        "label": "Geographic origin",
        "mandatory": True,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "collect.habitat",
        "label": "Isolation habitat",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "collect.habitat_ontobiotope",
        "label": "Ontobiotope term for the isolation habitat",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "genetics.gmo", "label": "GMO", "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "genetics.gmo_construction",
        "label": "GMO construction information",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "genetics.mutant_info",
        "label": "Mutant information",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "genetics.genotype",
        "label": "Genotype",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "genetics.sexual_state",
        "label": "Sexual state",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "genetics.ploidy",
        "label": "Ploidy",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "genetics.plasmids",
        "label": "Plasmids",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "genetics.plasmids_in_collections",
        "label": "Plasmids collections fields",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "publications",
        "label": "Literature",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "plant_pathogenicity_code",
        "label": "Plant pathogenicity code",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "pathogenity",
        "label": "Pathogenicity",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "enzyme_production",
        "label": "Enzyme production",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "production_of_metabolites",
        "label": "Production of metabolites",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "applications",
        "label": "Applications",
        "mandatory": False,
        "biolomics": {"field": "Applications", "type": "E"},
    },
    {
        "attribute": "remarks", "label": "Remarks", "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
    },
    {
        "attribute": "literature_linked_to_the_sequence_genome",
        "label": "Literature linked to the sequence/genome",
        "mandatory": False,
        # "biolomics": {"field": "MTA files URL", "type": "U"},
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
