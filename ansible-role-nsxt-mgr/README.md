ansible-role-nsxt-1st-mgr
=========================

This role works with NSX-T Manager version 2.5 and Ansible Modules v1.1.0 to deploy the 1st virtual appliance of an NSX-T Manager/Controller cluster.

Requirements
------------
* NSX-T version v2.5
* Ansible for NSX-T Modules v1.1.0 (check for dependencies here https://github.com/vmware/ansible-for-nsxt/blob/master/README.md)

Role Variables
--------------

`nsx_node1[hostname]`: Name for the virtual appliance.

`nsx_node1[mgmt_ip]`: IPv4 address for the port connected to the network management segment.

`nsx_username`: Initial administration account to use for the deployment. Default to "admin"

`nsx_password`: Initial administration password to use for the deployment. Has to be updated according to the standard password management process once deployment is completed.

`validate_certs`: Boolean to enable/disabel SSL certificate check.

`dep_size`: Deployment size for the virtual appliance. This will define the resources required for vCPU and Memory. Supported values are: "small", "medium" or "large".

`compute_cluster[portgroup]`: Name of the port group used for the management network segment.

`compute_cluster[datacenter]`: Name of the Datacenter object in vCenter where will be deployed the virtual appliance.

`compute_cluster[cluster]`: Name of the compute cluster object in vCenter where will be deployed the virtual appliance.

`compute_cluster[datastore]`: Name of the Datastore in the vCenter that will use the virtual appliance.

`compute_managers[mgmt_ip]`: IPv4 address of the vCenter appliance where the virtual appliance will be installed.

`compute_managers[username]`: UserID of the account to be used for the deployment of the virtual appliance.

`compute_managers[password]`: Password of the account to be used for the deployment of the virtual appliance.

`state`: Defines if it is a deployment or a decomission ("present"= deployment, "absent"=decomission).

`domain`: Is the DNS domain search.

`netmask`: Netmask for the network management segment where will be connected the virtual appliance.

`gateway`: IPv4 address of the gateway for the network management segment where will be connected the virtual appliance. 

`dns_server`: IPv4 address of a valid DNS server  

`ntp_server`: IPv4 address of a valid NTP source. 

Dependencies
------------
There must be connectivity between the software repository and the destination vCenter. Variables passed to the playbook must be in the correct format, because the role does not validate them.

The `library` and `module_utils` folders must be located within the role folder, or with the playbook, or set via an ansible.cfg file.

License
-------
(c) Roche

Author Information
------------------
Developed by N&FIT Engineering (glofct_dl-eng-network@msxdl.roche.com)