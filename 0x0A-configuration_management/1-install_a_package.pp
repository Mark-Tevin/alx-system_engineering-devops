# Install python3-pip package
package { 'python3-pip':
  ensure => installed,
}

# Install Flask 2.1.0 using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  unless  => '/usr/bin/pip3 show flask | grep Version | grep 2.1.0',
  require => Package['python3-pip'],
}
