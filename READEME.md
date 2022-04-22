# AGOL Batch Service Update Script

This script can be used to publish / overwrite every map in your ArcPro project (.aprx).

The base for this script is a [demo](https://pro.arcgis.com/en/pro-app/2.8/arcpy/sharing/featuresharingdraft-class.htm#GUID-FDFDD6D8-22BA-4693-A897-C9B10E07E931) on the ArcPro webpage. Additioanl functioanlity has been added to loop through all map in the project and create a hosted feature service or overwrite a hosted service. The script will also replace title, tag, summary, description, credits, and use limits with whatever is in the the metadata of the underlying feature class.

# Requirements
* ArcPro 2.9 and up
* AGOL role to create hosted feature services.

# Setup
1. Copy the script into a Notebook in ArcPro.
2. Within the script are five variables that need to be changed to get your setup up in running. These include:
    
    * **relPath** - Path to the aprx file
    * **user** - AGOL user name (needs a role that lets them add and edit hosted service.)
    * **password** - that users password
    * **outdir** - Path to a temporary folder. Used for staging the Service Definition of a service.
    * **portal** - Optional. Can be changed to a local portal address or a different AGOL organization.
3. Run the Notebook 