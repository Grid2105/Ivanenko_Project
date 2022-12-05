from SPARQLWrapper import SPARQLWrapper, JSON


class QueryGenerator:
    def __init__(self):
        self.sparql = SPARQLWrapper("https://dbpedia.org/sparql")

    def get_people(self, oblast, date_bottom, date_top):
        query = f''' 
            SELECT DISTINCT ?person
            WHERE  
            {{
                {{
                    ?person dbo:birthPlace/dbo:subdivision {oblast};
                            dbo:birthDate ?birth;
                            dbo:occupation | dbp:occupation ?profession. 
                    FILTER (CONTAINS(LCASE(STR(?profession)), "actor"))
                }}
                UNION
                {{
                    ?person dbo:birthPlace/dbo:subdivision {oblast};
                            dbo:birthDate ?birth;
                            dbo:occupation | dbp:occupation ?profession. 
                    FILTER (CONTAINS(LCASE(STR(?profession)), "actress"))
                }}
                UNION
                {{
                    ?person dbo:birthPlace ?city;
                            dbo:birthDate ?birth;
                            dbo:occupation | dbp:occupation ?profession. 
                    {oblast} dbp:seat ?city.
                    FILTER (CONTAINS(LCASE(STR(?profession)), "actor"))
                }}
                UNION
                {{
                    ?person dbo:birthPlace ?city;
                            dbo:birthDate ?birth;
                            dbo:occupation | dbp:occupation ?profession. 
                    {oblast} dbp:seat ?city.
                    FILTER (CONTAINS(LCASE(STR(?profession)), "actress"))
                }}
                FILTER (?birth > "{date_bottom}"^^xsd:date)
                FILTER (?birth < "{date_top}"^^xsd:date)
            }}
            ORDER BY ?person
        '''
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        result = self.sparql.query().convert()["results"]["bindings"]
        return [item["person"]["value"].replace("http://dbpedia.org/resource/", "") for item in result]

    def get_oblast(self):
        query = f''' 
            SELECT DISTINCT ?oblast STR(?originalName) AS ?name
            WHERE  {{
                ?oblast dbo:type dbr:Oblasts_of_Ukraine;
                            dbo:originalName ?originalName.
            }}
        '''
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        result = self.sparql.query().convert()["results"]["bindings"]
        oblastDict = {name: dbr for name, dbr in zip([item["name"]["value"] for item in result],
                                                     [item["oblast"]["value"].replace("http://dbpedia.org/resource/", "dbr:") for item in result])}
        return oblastDict

    def get_image(self, person):
        query = f''' 
                    SELECT DISTINCT ?image
                    WHERE {{
                        OPTIONAL {{ {person} dbo:thumbnail ?image. }}
                    }}
                '''
        # print(person)
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        image = self.sparql.query().convert()["results"]["bindings"]
        # print(image)
        return image

    def get_description(self, person):
        query = f''' 
            SELECT DISTINCT ?description
            WHERE {{
                OPTIONAL {{ {person} dbo:abstract|rdfs:comment ?description. }}
            }}
        '''
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        description = self.sparql.query().convert()["results"]["bindings"]
        return description

    def get_name(self, person):
        query = f''' 
            SELECT DISTINCT ?name
            WHERE {{
                OPTIONAL {{ {person} dbo:birthName|dbp:birthName|foaf:name|rdfs:label ?name. }}
            }}
        '''
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        name = self.sparql.query().convert()["results"]["bindings"]
        return name

    def get_birth_date(self, person):
        query = f''' 
            SELECT DISTINCT ?birthDate
            WHERE {{
                OPTIONAL {{ {person} dbo:birthDate|dbp:birthDate ?birthDate. }}
            }}
        '''
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        birthDate = self.sparql.query().convert()["results"]["bindings"]
        return birthDate

    def get_death_date(self, person):
        query = f''' 
            SELECT DISTINCT ?deathDate
            WHERE {{
                OPTIONAL {{ {person} dbo:deathDate|dbp:deathDate ?deathDate. }}
            }}
        '''
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        deathDate = self.sparql.query().convert()["results"]["bindings"]
        return deathDate

    def get_link(self, person):
        query = f''' 
            SELECT DISTINCT ?link
            WHERE {{
                OPTIONAL {{ {person} dbo:wikiPageExternalLink|prov:wasDerivedFrom|foaf:homepage|foaf:isPrimaryTopicOf ?link. }}
            }}
        '''
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        link = self.sparql.query().convert()["results"]["bindings"]
        return link

