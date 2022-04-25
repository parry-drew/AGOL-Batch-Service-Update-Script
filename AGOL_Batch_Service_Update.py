import arcpy
import os

 # Loctaion the ArcPro Project
relPath = <Path to your .aprx>
aprx = arcpy.mp.ArcGISProject(relPath)

#Inputs for Server Credentials
portal = "http://www.arcgis.com" # or local portal
user = <USER NAME> # user must have admin permissions to run
password = <PASSWORD>
shrOrg = False
shrEveryone = False
shrGroups = ""
outdir = <Path to a folder to stage the service definition>


# Sign in to portal
arcpy.SignInToPortal(portal, user, password)

# Loops through each map in the project
for m in aprx.listMaps():
    sd_fs_name = m.name
    print(sd_fs_name)
    
    # If you want to exclude some maps place your query to this loop.
    if "_QA" not in sd_fs_name: 
        # gets metadata info from the layer in each map
        layer = m.listLayers()[0]
        layer_metadata = layer.metadata
        
        #setup fortemp service definition
        sddraft_filename = sd_fs_name + ".sddraft"
        sddraft_output_filename = os.path.join(outdir, sddraft_filename)
        sd_filename = sd_fs_name + ".sd"
        sd_output_filename = os.path.join(outdir, sd_filename)

        # Create FeatureSharingDraft and set overwrite property. Uses map layer meta data to fill in tags.
        sddraft = m.getWebLayerSharingDraft("HOSTING_SERVER", "FEATURE", sd_fs_name)
        sddraft.summary = layer_metadata.summary
        sddraft.tags = layer_metadata.tags
        sddraft.description = layer_metadata.description
        sddraft.credits = layer_metadata.credits
        sddraft.useLimitations = "While we seek to provide accurate information, please note that errors may be present and information presented may not be complete. Accordingly, the City of New York or the New York City Department of Transportation make no representation as to the accuracy of the information or its suitability for any purpose and disclaim any liability for omissions or errors that may be contained therein."
        sddraft.overwriteExistingService = True

        # Create Service Definition Draft file
        sddraft.exportToSDDraft(sddraft_output_filename)

        # Stage Service
        print("Start Staging {0}".format(sd_fs_name))
        arcpy.StageService_server(sddraft_output_filename, sd_output_filename)

        # Share to portal
        print("Start Uploading {0}".format(sd_fs_name))
        arcpy.UploadServiceDefinition_server(sd_output_filename, "HOSTING_SERVER")

        print("Finish Publishing {0}".format(sd_fs_name))

print("Finish Publishing Script Complete")

