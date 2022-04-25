# AGOL Batch Service Update Script

This script can be used to publish / overwrite every map in your ArcPro project (.aprx).

The base for this script comes from a [demo](https://pro.arcgis.com/en/pro-app/2.8/arcpy/sharing/featuresharingdraft-class.htm#GUID-FDFDD6D8-22BA-4693-A897-C9B10E07E931)on the ArcPro webpage. Additioanl functioanlity has been added to loop through all map in the project and create or overwrite a hosted feature service. The script will also replace title, tag, summary, description, credits, and use limits with whatever is in the the metadata of the underlying feature class.

This script makes the following assumption that each map in your project contains one layer:
1. Each map in your project has one layer.
2. If a map name has the substring "_QA" it will not be processed.


# Requirements
* ArcPro 2.9 and up
* AGOL role to create and edit hosted feature services.

# Notebook Setup
This ```AGOL_Batch_Service_Upday.py``` script is useful if want to run the script on a task scheduler. One draw back is that login credentials need to be hard coded into the script.

1. Copy the ```AGOL_Batch_Service_Update.py``` script into a Notebook in ArcPro.
2. Within the script are five variables that need to be changed to get your setup up in running. These include:
    
    * **relPath** - Path to the aprx file
    * **user** - AGOL user name (needs a role that lets them add and edit hosted service.)
    * **password** - That users password
    * **outdir** - Path to a temporary folder. Used for staging the Service Definition of a service.
    * **portal** - Optional. Can be changed to a local portal address or a different AGOL organization.

3. There area few additional parameters than can also be changed if you want control over the sharing of the hosted feature service:
    * **shrOrg** - Mark as ```True``` if you want to share with the enitire organization.
    * **shrEveryone** - Mark ```True``` if you want the data to be public.
    * **shrGroups** - Assign any groups that should have access.
4. Run the Notebook 
5. Optional, run on task scheduler to keep the hosted feature updated.

# Script Tool Setup
This ```Batch_Service_Update_ScriptTool.py``` script is useful for run the script from ArcPro toolbox. This tool will rerquire you manually enter your AGOL credentials as an input.

1. The easiest way to install this tool is to copy the ```.tbx``` or ```.atbx``` toolbox into your project folder.
2. Double click on the ```Batch-Service_Update``` tool and fill in the inputs.

3. If you want to create the tool from scrap use the ```Batch_Service_Update_ScriptTool.py``` and follow the directions outline [here](https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/adding-a-script-tool.htm). Your parameters should look like this:

|  | Label          | Name           | Data Type     | Type     | Directions |
|---|----------------|----------------|---------------|----------|------------|
| 0 | Path to aprx   | Path_to_aprx   | File          | Required | Input      |
| 1 | Staging Folder | Staging_Folder | Folder        | Required | Input      |
| 2 | Username       | Username       | String        | Required | Input      |
| 3 | Password       | Password       | String Hidden | Required | Input      |


