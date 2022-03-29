ansible-role-nsxt-nodes
=========================

This role works with NSX-T Manager version 2.5 and Ansible Modules v1.1.0 to deploy NSX-T in the different type of nodes: Transport and Edge (the latter just for VM form factor). It works going through the list of nodes, in a loop. Every variable with the "item." prefix refers to one element of the list (one transport or edge node).

Requirements
------------
* NSX-T version v2.5
* Ansible for NSX-T Modules v1.1.0 (check for dependencies here https://github.com/vmware/ansible-for-nsxt/blob/master/README.md)

Role Variables
--------------

`nsx_mgr_vip`: Name for the virtual appliance.

`nsx_username`: Initial administration account to use for the deployment. Default to "admin"

`nsx_password`: Initial administration password to use for the deployment. Has to be updated according to the standard password management process once deployment is completed.

`validate_certs`: Boolean to enable/disabel SSL certificate check.

`item.display_name`:  Name of the object

`host_switch_profiles`: Different configuration profiles to be used to set up the NVDS switch 

`item.node_deployment_info.resource_type`: Type of node to be deployed: HostNode or EdgeNode

`pnics`: Port mappings for physical NICs

`transport_nodes`: List of Nodes where to deploy NSX-T

`item.ip_assignment_spec`: IP pools from where the TEP IPs addresses will be taken

`transport_zone_endpoints`: Transport Zone that will host the TEPs

`item.node_deployment_info`: Data structure that collects a number of the configuration vriables to be used for the deployment to be passed to the Ansible module. Check here for more info https://github.com/vmware/ansible-for-nsxt/blob/master/library/nsxt_transport_nodes.py

`state`: Defines if it is a deployment or a decomission ("present"= deployment, "absent"=decomission).

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