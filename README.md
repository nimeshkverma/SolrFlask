# SolrFlask

# Standard Input Json Format specifying solr query parameters
```
{
	"filters": {
		"type" : "array",
		"value" : 
		[
			{
				"type" : "json",
				"value" : {
					"not_query" : {
						"type" : "boolean",
						"value" : false
					}, 
					"fields" : {
						"type" : "json",
						"value" : {
							"feed_id" : {
								"type" : "int",
								"value" : 123
							}, 
							"price" : {
								"type" : "array",
								"value" : [
									123,
									456,
									789
								]
							},
							"somefield" : {
								"type" : "json",
								"value" : {
									"min" : { 
										"type" : "int",
										"value" : 123
									},
									"max" : { 
										"type" : "int",
										"value" : 123
									}
								}
							}
						}
					}
				}
			}
		]
	}, 
	"order" : {
		"type" : "json",
		"value" : {
			"asc" : {
				"type" : "array",
				"value" : [
					"feed_id",
					"price"
				]
			}, 
			"desc" : {
				"type" : "array",
				"value" : [
					"somefield",
					"otherfield"
				]
			}
		}
	},
	"aggregations" : {
		"type" : "json",
		"value" : {
			"is_global" : {
				"type" : "boolean",
				"value" : false
			},
			"fields" : {
				"type" : "json",
				"value" : {
					"count" : {
						"type" : "array",
						"value" : [
							"field1",
							"field2"
						]
					}
				}
			}
		}
	}
}
```
