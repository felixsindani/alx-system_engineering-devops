#installs flask
exec { 'install_flask_2.1.0':
  command => '/usr/bin/pip3 install flask==2.1.0',
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  path    => ['/usr/bin', '/bin'],
}

