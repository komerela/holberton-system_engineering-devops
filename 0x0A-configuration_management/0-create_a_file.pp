# puppet script creates new file with content
file { '/tmp/holberton':
  content => 'I love Puppet',
  mode => '0744',
  owner => www-data,
  group => www-data,
}
