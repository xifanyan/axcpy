# ADP Task Types Reference

This document provides a comprehensive list of all task types available in the ADP API specification, along with their descriptions.

## Task Types

### 1. Add Fields
**Description:** Adds fields to an index.

### 2. Add Subengine
**Description:** Adds sub-engine to an existing application.

### 3. APWT Check Config
**Description:** Runs sanity checks on crawlers and features.

### 4. APWT Clear Fields
**Description:** Clears fields as marked by the clearMaker.

### 5. APWT Compute Chains
**Description:** Computes chain files (concatenation of agreements and amendments).

### 6. APWT Failed Documents Checker
**Description:** Checks for documents that failed during processing.

### 7. APWT Generate Csv
**Description:** Generates CSV files (normal agreements, umbrella funds) from the given agreements.

### 8. APWT Image to PDF A Converter
**Description:** Convert images to PDF-A files.

### 9. APWT OCR
**Description:** Executes OCR on chain files.

### 10. APWT Parse and Validate
**Description:** Runs a native task in its onw process.

### 11. APWT Self Service Processor
**Description:** Perceptiv Self Service specifiv data manipulations.

### 12. APWT Standalone Amendment Post Processor
**Description:** Post processing for standalone procsessing request.

### 13. APWT Workflow Synchronization
**Description:** Synchronizes APWT workflows based on agreement id and target engine.

### 14. APWT ZIP
**Description:** Compress PDF files into a ZIP archive.

### 15. Axcelerate Application Lock
**Description:** (Un)Lock an Axclerate NG project.

### 16. Axcelerate Delete
**Description:** Delete Axclerate NG data for a particular project.

### 17. Axcelerate Export
**Description:** Export Axclerate NG data for a particular project.

### 18. Axcelerate Import
**Description:** Import Axclerate NG data for a particular project.

### 19. Axcelerate Remove Bootstrap Information
**Description:** Sets bootstrap information for Axclerate NG project.

### 20. Axcelerate Set Bootstrap Information
**Description:** Sets bootstrap information for Axclerate NG project.

### 21. CLI
**Description:** Runs a native task in its own process.

### 22. CSV Column Alias
**Description:** Transforms CSV columns based on an alias file.

### 23. CSV Column Filter
**Description:** Creates a new csv file with a column subset of the original csv file.

### 24. CSV Column Type Detection
**Description:** Detects column types of a specified csv-file.

### 25. CSV Converter
**Description:** Converts data from the dynamic table data service to a new csv file.

### 26. CSV Copy Header
**Description:** Task to copy the header of a CSV file.

### 27. CSV Detection
**Description:** Auto detects csv file criterias.

### 28. CSV File Reduction
**Description:** Reduces a source file (csv) to a smaller excerpt.

### 29. CSV Loadfile Normalizer
**Description:** Normalizes given csv to a new csv file.

### 30. CSV Merge
**Description:** Merges metaData or natives/images by using a csv file.

### 31. CSV Multivalue Separator Detection
**Description:** Auto detects csv mulivalue separators.

### 32. CSV Validation
**Description:** Validates a csv file.

### 33. Cancel Publish
**Description:** This task cancels publishing a matter into Review, Investigation or ECA applications. It cancels all publishing processes currently running for the specified matter. Some documents in the source engine might be tagged with categories from the cancelled publish processes.

### 34. Change Display Name
**Description:** Changes the display name of an application.

### 35. Change Field Contents
**Description:** Change meta data or text type contents in a configured engine.

### 36. Check for entity status
**Description:** Retrieves a status of a given entity (data source, application or engine).

### 37. Clear Artifacts
**Description:** Clears ADP task artifacts like log-files, meta-data files, validation reports etc.

### 38. Compute Counts
**Description:** Compute Counts.

### 39. Configure Data Source
**Description:** Configures a data source.

### 40. Configure Engine Security
**Description:** Task to define field, folder and document level security.

### 41. Configure Entity
**Description:** Configures an entity.

### 42. Configure Hosts in Workspaces
**Description:** Configure 'add hosts automatically to workspace' and add/remove hosts to/from workspaces.

### 43. Configure Service Properties
**Description:** Configures service properties.

### 44. Consumer Trigger
**Description:** Empty Task to trigger message consumers.

### 45. Convert Opticon To Csv
**Description:** Converts an Opticon file to CSV format.

### 46. Crawler Monitoring
**Description:** Monitors a set of crawlers and waits for completion/failure of all crawlers.

### 47. Create Application
**Description:** Creates an application.

### 48. Create Custodian
**Description:** Creates a custodian from the given input parameters.

### 49. Create Data Source
**Description:** Creates a new data source.

### 50. Create Investigation
**Description:** This task creates Investigation applications using MatterSpecific web-service.

### 51. Create OCR Job
**Description:** Changes metaData by using regEx replacement.

### 52. Create Review Interface
**Description:** *(No description provided)*

### 53. Create Workspace
**Description:** Creates a workspace.

### 54. Data Model Synchronization
**Description:** Syncronizeds field tables of source and target data models.

### 55. Delete Storages
**Description:** Deletes engine storages.

### 56. Enable Bucket
**Description:** Enables or disables the specified bucket.

### 57. Engine Job Monitoring
**Description:** Monitor/list engine jobs.

### 58. Export
**Description:** Interface to exportApplicationTree.

### 59. Export Documents
**Description:** Export documents in CSV format.

### 60. Export Ingestion Report
**Description:** Task to export ingestion report.

### 61. Export Matter
**Description:** Export matter.

### 62. Export Storage
**Description:** Exports the storage of a project.

### 63. Export Storage Locations
**Description:** Interface to exportStorageLocations.

### 64. Export Tagger Global Searches
**Description:** Exports global searches associated with taggers of a project.

### 65. Extract Zip
**Description:** Extracts a Zip to a target location.

### 66. Global Searches
**Description:** Manage Global Searches.

### 67. Health
**Description:** Retrieves ADP end-point system health attributes.

### 68. Import
**Description:** Interface to importApplicationTree.

### 69. Import Storage
**Description:** Imports storages of a project.

### 70. Import Storage Locations
**Description:** Interface to importStorageLocations.

### 71. Insert Documents
**Description:** Insert documents into an engine.

### 72. List Bucket
**Description:** Returns a JSON list of the entries of the specified bucket.

### 73. List Entities
**Description:** Writes a list of entities ot an output variable.

### 74. List Entity Ids
**Description:** Writes a list of entity ids and optionally their related entity ids into an output variable.

### 75. Manage Core Host Roles
**Description:** Mangage core roles for a host.

### 76. Manage Host Roles
**Description:** Mangage roles for a host.

### 77. Manage Taggers
**Description:** Install and uninstall taggers.

### 78. Manage Taxonomy
**Description:** Performs actions on a taxonomy like creating or updating categories, removing categories and quering categories.

### 79. Manage Users and Groups
**Description:** Creates users, creates groups, assign users to group and set roles of users and groups in applications.

### 80. Matter Entities
**Description:** Task to manage matter specific entities.

### 81. Matter Management
**Description:** *(No description provided)*

### 82. Matter Report
**Description:** Task to export matter reports.

### 83. Meta Data Changer
**Description:** Changes metaData by using regEx replacement.

### 84. Move Files
**Description:** Move files to defined folders depending on results of workflow and tasks.

### 85. No Operation
**Description:** No operation task.

### 86. PSS Create CSV Files
**Description:** Creates the Perceptiv CSV Files.

### 87. PSS Create FieldTypes
**Description:** Creates the Perceptiv FieldTypes-File.

### 88. PSS Create MindserverConfig
**Description:** Creates the Perceptiv MindserverConfig.

### 89. PSS Create XHTML Files
**Description:** Creates the Perceptiv XHTML Files.

### 90. PSS Read Self-Service Configuration
**Description:** Reads configuration from self-service back-end.

### 91. PSS Trigger DB Back-up
**Description:** Triggers PSS DB back-up.

### 92. PSS Validate Model
**Description:** Validates the Model for Consistency.

### 93. Ping Project
**Description:** Pings applications or engines.

### 94. Publish To Investigation
**Description:** This task publishes documents from a matter into the Investigation application using MatterSpecific web-service.

### 95. Publish To Review
**Description:** *(No description provided)*

### 96. Purge History
**Description:** Purges ADP task data base history.

### 97. Query Engine
**Description:** Queries an engine.

### 98. Query Postgresql DB
**Description:** Queries postgresql databases.

### 99. Read Configuration
**Description:** A Task to read configurations into JSON or XML.

### 100. Read Documents
**Description:** Read documents.

### 101. Read Service Alerts
**Description:** Changes the display name of an application.

### 102. Read from LDAP
**Description:** Reads meta data and many more from an LDAP source.

### 103. Receive meta data from database
**Description:** Creates or overrides new meta data key/value pairs from database values for the workflow.

### 104. Receive meta data from file
**Description:** Creates or overrides new meta data key/value pairs from a properties file for the workflow.

### 105. Remote Process Status
**Description:** Task to upload a status information file to the cloud.

### 106. Remove Processes
**Description:** Removes processes.

### 107. Restart Processes
**Description:** Restarts processes.

### 108. Save Engines
**Description:** Saves engines.

### 109. Search Based Enrichment
**Description:** Search Based Enrichment.

### 110. Skip on value
**Description:** Task that will execute a java script condition and will jump to another task in the case the script returns true.

### 111. Split Csv Data Source
**Description:** Splits a CSV data source into chunks producing multiple data sources if necessary.

### 112. Start Application
**Description:** Starts an application.

### 113. Start Data Source
**Description:** Starts a data source.

### 114. Start Elastic Crawler Hosts
**Description:** Starts elastic crawler hosts.

### 115. Start Workflow
**Description:** Task that will start an ADP workflow.

### 116. Stop Processes
**Description:** Stops processes.

### 117. Suspend Data Source
**Description:** Suspends and resumes data sources.

### 118. Taxonomy Statistic
**Description:** Retrieves category counts for a taxonomy.

### 119. Write Configuration
**Description:** A Task to write configurations from JSON.

### 120. XPath
**Description:** Evaluates a set of XPath expressions on an XML document.

---

**Total Task Types:** 120