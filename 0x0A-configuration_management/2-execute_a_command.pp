# script kills process killmenow
exec { 'pkill':
  command => '/usr/bin/pkill killmenow'
}

