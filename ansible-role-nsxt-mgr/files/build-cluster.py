#!/usr/bin/env python3


from __future__ import absolute_import, division, print_function
__metaclass__ = type

import sys
import json, time
from ansible.module_utils.basic import AnsibleModule
from vmware_nsxt import vmware_argument_spec, request
from ansible.module_utils._text import to_native

def main():
  argument_spec = vmware_argument_spec()
  #module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)
  
  mgr_hostname = sys.argv[1] #module.params['hostname']
  mgr_username = sys.argv[2] #module.params['username']
  mgr_password = sys.argv[3] #module.params['password']
  if sys.argv[7] == "False":
    validate_certs = bool("")
  else:
    validate_certs = bool("True")
  #validate_certs = False #module.params['validate_certs']
  manager_url = 'https://{}/api/v1'.format(mgr_hostname)

  new_nodes = []
  new_nodes.append(sys.argv[4])
  new_nodes.append(sys.argv[5])

  vip = sys.argv[6]

  #changed = False
  try:
    (rc, resp) = request(manager_url+ '/cluster/nodes/status', headers=dict(Accept='application/json'),
                    url_username=mgr_username, url_password=mgr_password, validate_certs=validate_certs, ignore_errors=True)
  except Exception as err:
    #module.fail_json(msg='Error accessing cluster runtime status. Error [%s]' % (to_native(err)))
    print('Error accessing cluster runtime status. Error [%s]' % err)
  
  json_resp = json.dumps(resp)
  parsed_resp = json.loads(json_resp)
  print(parsed_resp['management_cluster'][0]['role_config']['api_listen_addr']['certificate_sha256_thumbprint'])
  api_cert_thumbprint = parsed_resp['management_cluster'][0]['role_config']['api_listen_addr']['certificate_sha256_thumbprint']
  mgr_ip = parsed_resp['management_cluster'][0]['role_config']['api_listen_addr']['ip_address']
  #module.exit_json(changed=changed, **resp)

  try:
    (rc, resp) = request(manager_url+ '/cluster/status', headers=dict(Accept='application/json'),
                    url_username=mgr_username, url_password=mgr_password, validate_certs=validate_certs, ignore_errors=True)
  except Exception as err:
    #module.fail_json(msg='Error accessing cluster status. Error [%s]' % (to_native(err)))
    print('Error accessing cluster status. Error [%s]' % err)

  json_resp = json.dumps(resp)
  parsed_resp = json.loads(json_resp)
  print(parsed_resp['cluster_id'])
  new_cluster_id = parsed_resp['cluster_id']
  #module.exit_json(changed=changed, **resp)

  headers = dict(Accept="application/json")
  headers['Content-Type'] = 'application/json'
  body =  {'cluster_id': new_cluster_id, 'ip_address': mgr_ip, 'username': mgr_username, 'password': mgr_password, 'certficate_sha256_thumbprint': api_cert_thumbprint}

  for i in new_nodes:
    new_node = i
    new_node_url = 'https://{}/api/v1'.format(new_node)
    request_data = json.dumps(body)
    try:
      (rc, resp) = request(new_node_url+ '/cluster?action=join_cluster', data=request_data, headers=headers, method='POST',
                    url_username=mgr_username, url_password=mgr_password, validate_certs=validate_certs, ignore_errors=True)
    except Exception as err:
      #module.fail_json(msg='Failed to add node to the cluster. Request body [%s]. Error[%s].' % (request_data, to_native(err)))
      print('Failed to add node to the cluster. Error[%s].' % err)

    time.sleep(300)

  try:
    (rc, resp) = request(manager_url+ '/cluster/api-virtual-ip?action=set_virtual_ip&ip_address='+ vip, method='POST',
                    url_username=mgr_username, url_password=mgr_password, validate_certs=validate_certs, ignore_errors=True)
  except Exception as err:
    #module.fail_json(msg='Failed to add virtual IP to the cluster. Error[%s].' % (to_native(err)))
    print('Failed to add virtual IP to the cluster. Error[%s].' % err)

  try:
    (rc, resp) = request(manager_url+ '/cluster/status', headers=dict(Accept='application/json'),
                    url_username=mgr_username, url_password=mgr_password, validate_certs=validate_certs, ignore_errors=True)
  except Exception as err:
    #module.fail_json(msg='Error accessing cluster status. Error [%s]' % (to_native(err)))
    print('Error accessing cluster status. Error [%s]' % err)

  json_resp = json.dumps(resp)
  parsed_resp = json.loads(json_resp)
  print(parsed_resp['mgmt_cluster_status']['status'])
  #module.exit_json(changed=changed, **resp)

if __name__ == '__main__':
	main()