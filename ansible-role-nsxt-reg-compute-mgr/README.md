ansible-role-nsxt-reg-compute-mgr
=========================

This role works with NSX-T Manager version 2.5 and Ansible Modules v1.1.0 to register Compute Managers to the first virtual appliance of an NSX-T Manager/Controller cluster. 

Requirements
------------
* NSX-T version v2.5
* Ansible for NSX-T Modules v1.1.0 (check for dependencies here https://github.com/vmware/ansible-for-nsxt/blob/master/README.md)

Role Variables
--------------

`nsx_node1[mgmt_ip]`: IPv4 address for the port connected to the network management segment.

`nsx_username`: Initial administration account to use for the deployment. Default to "admin"

`nsx_password`: Initial administration password to use for the deployment. Has to be updated according to the standard password management process once deployment is completed.

`validate_certs`: Boolean to enable/disabel SSL certificate check.

`compute_managers[display_name]`: Name of the vCenter appliance to be registered.

`compute_managers[mgmt_ip]`: IPv4 address or FQDN of the vCenter appliance to be registered.

`compute_managers[username]`: UserID of the account to be used for the registration.

`compute_managers[password]`: Password of the account to be used for the registration.

`compute_managers[origin_type]`: Default to "vCenter"

`compute_managers[credential_type]`: Default to "UsernamePasswordLoginCredential"

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