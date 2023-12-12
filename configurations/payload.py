import json


payload_host_get_params = {
			"output":"extend",
			"selectInterFaces":["interfachid", "name", "type","duplex", "vlans", "dns", "ip", "macaddress"],
			"selectGraphs":["graogid", "height", "name","width","flags","graphtype", "percent_right","percent_left", "show_3d", "show_legend", "show_work_period", "show_truggers","templateid" ],
			"selectItems":["itemid", "name", "key_", "lastvalue", "units","description","status","value_type", "delay","error", "history","status_code"],
			"selectInventory":["inventoryid", "type", "name", "ket_", "perentid", "lastvalue", "units"],
			"key_":["system.cpu.load"],
			"selectTriggers":["triggerid", "description", "expression","lastchange", "status" , "value"],
		}

