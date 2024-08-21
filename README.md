# Kubestronaut Prep

## This is in no way endorsed or approved by the Linux Foundation or the Cloud Native Computing Foundation.
This repo is only used by me to test out various scenarios I've seen in courses, real life, and based on the domains and competencies for the actual exams.

### CKA Prep

### CKAD Prep

### CKS Prep -- Note after 12 Sept the exam will change.
#### Test 1
Ensure that "connectivity-test-pod" can connect to the "web-server pod".  
**DO NOT** re-create, change, or delete resources already created in the namespace.

If you are done or if you are stuck, you can find the example in the **solutions folder: test-1**  

#### Test 2
Ensure that "ns-connectivity-test-pods" can connect to the "web-server pod".  
The connection needs open for all namespaces but limited to the labels on the "ns-connectivity-pods".   
**DO NOT** re-create, change, or delete resources already created in the namespaces.

If you are done or if you are stuck, you can find the example in the **solutions folder: test-2**  
  
#### Test 3
On the **controlplane** node has kube-bench been installed.  
Every minute a new report is being generated and published via a pod running in the **kube-bench** namespace. The pod is exposed via a nodeport service.  

Find out what the right port is and open the report in your webbrowser.  
Fix the following items from the report:  
*1.2.15 Ensure that the --profiling argument is set to false (Automated)*  
*1.2.29 Ensure that the API Server only makes use of Strong Cryptographic Ciphers*  
*4.2.12 Ensure that the Kubelet only makes use of Strong Cryptographic Ciphers*  
  
**Additionally:**  
Ensure that ETCD, API Server and the kubelets can communicate with the following TLS version and Ciphers:  
Minimum TLS version: 1.2  
Allowed TLS Ciphers: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 & TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384