storage "file" {
  path = "/vault/file"
}

listener "tcp" {
  address       = "0.0.0.0:8200"
  tls_cert_file = "/etc/vault/ssl/vault.crt"
  tls_key_file  = "/etc/vault/ssl/vault.key"
}

ui = true