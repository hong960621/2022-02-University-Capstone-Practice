from pymatgen.ext.matproj import MPRester
    
MPR = MPRester("MlcWrm13T2xvfyLR")
### watashino api key desu G39tJ82PiRrrg2QIxbfyvbaat375Y4wf
    
criteria = {'elements':{"$in":["P", "Sn"], "$all": ["S","Li"]}, #All compounds contain O, and must have Li or Na or K
            'nelements':3,
             # 'icsd_ids': {'$gte': 0},
            'e_above_hull': {'$lte': 0.01},
            # 'anonymous_formula': {"A": 1, "B": 1, "C": 3},
            "band_gap": {"$gt": 0.2}               
             }
    
            # The properties and the criteria use MaterialsProject features 
            # You can see what is queryable from the MP API documentation: 
            # https://github.com/materialsproject/mapidoc/tree/master/materials
            
            # The criteria uses mongodb query language. See here 
            # for more details: https://docs.mongodb.com/manual/reference/operator/query/
    
props = ['structure', "material_id",'pretty_formula','e_above_hull',"band_gap","band_structure"]
entries = MPR.query(criteria=criteria, properties=props)
    
print(len(entries))
    
for e in entries:
    print(e['pretty_formula'])
    print(e['band_gap'])
    print(e)
    # break