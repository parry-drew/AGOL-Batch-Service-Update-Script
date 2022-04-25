import arcpy, os
def ScriptTool(param0, param1, param2, param3):
    relPath = param0
    aprx = arcpy.mp.ArcGISProject(relPath)
    portal = "https://nycdot.maps.arcgis.com" 
    user = param2
    password = param3
    shrOrg = False
    shrEveryone = False
    shrGroups = ""
    outdir = param1
    
    # Sign in to portal
    arcpy.SignInToPortal(portal, user, password)
    for m in aprx.listMaps():
        sd_fs_name = m.name
        print(sd_fs_name)
        
        if "_QA" not in sd_fs_name: 
            layer = m.listLayers()[0]
            layer_metadata = layer.metadata
            
            sddraft_filename = sd_fs_name + ".sddraft"
            sddraft_output_filename = os.path.join(outdir, sddraft_filename)
            sd_filename = sd_fs_name + ".sd"
            sd_output_filename = os.path.join(outdir, sd_filename)
            sddraft = m.getWebLayerSharingDraft("HOSTING_SERVER", "FEATURE", sd_fs_name)
            sddraft.summary = layer_metadata.summary
            sddraft.tags = layer_metadata.tags
            sddraft.description = layer_metadata.description
            sddraft.credits = layer_metadata.credits
            sddraft.useLimitations = "While we seek to provide accurate information, please note that errors may be present and information presented may not be complete. Accordingly, the City of New York or the New York City Department of Transportation make no representation as to the accuracy of the information or its suitability for any purpose and disclaim any liability for omissions or errors that may be contained therein."
            sddraft.overwriteExistingService = True
            
            sddraft.exportToSDDraft(sddraft_output_filename)
            
            print("Start Staging {0}".format(sd_fs_name))
            arcpy.StageService_server(sddraft_output_filename, sd_output_filename)
            
            print("Start Uploading {0}".format(sd_fs_name))
            arcpy.UploadServiceDefinition_server(sd_output_filename, "HOSTING_SERVER")
            print("Finish Publishing {0}".format(sd_fs_name))
    print("Finish Publishing")
    
    return
if __name__ == '__main__':
    param0 = arcpy.GetParameterAsText(0)
    param1 = arcpy.GetParameterAsText(1)
    param2 = arcpy.GetParameterAsText(2)
    param3 = arcpy.GetParameterAsText(3)
    
    ScriptTool(param0, param1, param2, param3)
    print(param0)
    
    # Update derived parameter values using arcpy.SetParameter() or arcpy.SetParameterAsText()
