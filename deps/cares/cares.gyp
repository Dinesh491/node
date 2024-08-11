{
  'variables': {
    'cares_sources_common': [
      'include/ares.h',
      'include/ares_dns.h',
      'include/ares_dns_record.h',
      'include/ares_nameser.h',
      'include/ares_version.h',
      'src/lib/ares__addrinfo2hostent.c',
      'src/lib/ares__addrinfo_localhost.c',
      'src/lib/ares__close_sockets.c',
      'src/lib/ares__hosts_file.c',
      'src/lib/ares__parse_into_addrinfo.c',
      'src/lib/ares__socket.c',
      'src/lib/ares__sortaddrinfo.c',
      'src/lib/ares_android.c',
      'src/lib/ares_android.h',
      'src/lib/ares_cancel.c',
      'src/lib/ares_cookie.c',
      'src/lib/ares_data.c',
      'src/lib/ares_data.h',
      'src/lib/ares_destroy.c',
      'src/lib/ares_free_hostent.c',
      'src/lib/ares_free_string.c',
      'src/lib/ares_freeaddrinfo.c',
      'src/lib/ares_getaddrinfo.c',
      'src/lib/ares_getenv.c',
      'src/lib/ares_getenv.h',
      'src/lib/ares_gethostbyaddr.c',
      'src/lib/ares_gethostbyname.c',
      'src/lib/ares_getnameinfo.c',
      'src/lib/ares_inet_net_pton.h',
      'src/lib/ares_init.c',
      'src/lib/ares_ipv6.h',
      'src/lib/ares_library_init.c',
      'src/lib/ares_metrics.c',
      'src/lib/ares_options.c',
      'src/lib/ares_platform.c',
      'src/lib/ares_platform.h',
      'src/lib/ares_private.h',
      'src/lib/ares_process.c',
      'src/lib/ares_qcache.c',
      'src/lib/ares_query.c',
      'src/lib/ares_search.c',
      'src/lib/ares_send.c',
      'src/lib/ares_setup.h',
      'src/lib/ares_strerror.c',
      'src/lib/ares_sysconfig.c',
      'src/lib/ares_sysconfig_files.c',
      'src/lib/ares_timeout.c',
      'src/lib/ares_update_servers.c',
      'src/lib/ares_version.c',
      'src/lib/dsa/ares__array.c',
      'src/lib/dsa/ares__array.h',
      'src/lib/dsa/ares__htable.c',
      'src/lib/dsa/ares__htable.h',
      'src/lib/dsa/ares__htable_asvp.c',
      'src/lib/dsa/ares__htable_asvp.h',
      'src/lib/dsa/ares__htable_strvp.c',
      'src/lib/dsa/ares__htable_strvp.h',
      'src/lib/dsa/ares__htable_szvp.c',
      'src/lib/dsa/ares__htable_szvp.h',
      'src/lib/dsa/ares__htable_vpvp.c',
      'src/lib/dsa/ares__htable_vpvp.h',
      'src/lib/dsa/ares__llist.c',
      'src/lib/dsa/ares__llist.h',
      'src/lib/dsa/ares__slist.c',
      'src/lib/dsa/ares__slist.h',
      'src/lib/event/ares_event.h',
      'src/lib/event/ares_event_configchg.c',
      'src/lib/event/ares_event_epoll.c',
      'src/lib/event/ares_event_kqueue.c',
      'src/lib/event/ares_event_poll.c',
      'src/lib/event/ares_event_select.c',
      'src/lib/event/ares_event_thread.c',
      'src/lib/event/ares_event_wake_pipe.c',
      'src/lib/event/ares_event_win32.c',
      'src/lib/event/ares_event_win32.h',
      'src/lib/inet_net_pton.c',
      'src/lib/inet_ntop.c',
      'src/lib/legacy/ares_create_query.c',
      'src/lib/legacy/ares_expand_name.c',
      'src/lib/legacy/ares_expand_string.c',
      'src/lib/legacy/ares_fds.c',
      'src/lib/legacy/ares_getsock.c',
      'src/lib/legacy/ares_parse_a_reply.c',
      'src/lib/legacy/ares_parse_aaaa_reply.c',
      'src/lib/legacy/ares_parse_caa_reply.c',
      'src/lib/legacy/ares_parse_mx_reply.c',
      'src/lib/legacy/ares_parse_naptr_reply.c',
      'src/lib/legacy/ares_parse_ns_reply.c',
      'src/lib/legacy/ares_parse_ptr_reply.c',
      'src/lib/legacy/ares_parse_soa_reply.c',
      'src/lib/legacy/ares_parse_srv_reply.c',
      'src/lib/legacy/ares_parse_txt_reply.c',
      'src/lib/legacy/ares_parse_uri_reply.c',
      'src/lib/record/ares_dns_mapping.c',
      'src/lib/record/ares_dns_multistring.c',
      'src/lib/record/ares_dns_multistring.h',
      'src/lib/record/ares_dns_name.c',
      'src/lib/record/ares_dns_parse.c',
      'src/lib/record/ares_dns_private.h',
      'src/lib/record/ares_dns_record.c',
      'src/lib/record/ares_dns_write.c',
      'src/lib/str/ares__buf.c',
      'src/lib/str/ares__buf.h',
      'src/lib/str/ares_str.c',
      'src/lib/str/ares_str.h',
      'src/lib/str/ares_strcasecmp.c',
      'src/lib/str/ares_strcasecmp.h',
      'src/lib/str/ares_strsplit.c',
      'src/lib/str/ares_strsplit.h',
      'src/lib/util/ares__iface_ips.c',
      'src/lib/util/ares__iface_ips.h',
      'src/lib/util/ares__threads.c',
      'src/lib/util/ares__threads.h',
      'src/lib/util/ares__timeval.c',
      'src/lib/util/ares_math.c',
      'src/lib/util/ares_rand.c',
      'src/tools/ares_getopt.c',
      'src/tools/ares_getopt.h',
    ],
    'cares_sources_mac': [
      'config/darwin/ares_config.h',
      'src/lib/ares_sysconfig_mac.c',
      'src/lib/thirdparty/apple/dnsinfo.h',
    ],
    'cares_sources_win': [
      'src/lib/ares_sysconfig_win.c',
      'src/lib/config-win32.h',
      'src/lib/windows_port.c',
    ],
  },

  'target_defaults': {
    'conditions': [
      ['OS!="win"', {
        'defines': [
          '_DARWIN_USE_64_BIT_INODE=1',
          '_LARGEFILE_SOURCE',
          '_FILE_OFFSET_BITS=64',
          '_GNU_SOURCE'
        ]
      }],
      [ 'OS in "aix os400"', {
        'include_dirs': [ 'config/aix' ],
        'sources': [ 'config/aix/ares_config.h' ],
        'defines': [
          # Support for malloc(0)
          '_LINUX_SOURCE_COMPAT=1',
          '_ALL_SOURCE=1'],
      }],
      ['OS=="solaris"', {
        'defines': [
          '__EXTENSIONS__',
          '_XOPEN_SOURCE=500'
        ]
      }]
    ]
  },

  'targets': [
    {
      'target_name': 'cares',
      'type': '<(library)',
      'include_dirs': [ 'include', 'src/lib' ],
      'direct_dependent_settings': {
        'include_dirs': [ 'include' ],
        'cflags': [ '-Wno-error=deprecated-declarations' ],
        'conditions': [
          [ 'OS=="mac"', {
            'xcode_settings': {
              'OTHER_CFLAGS': [ '-Wno-error=deprecated-declarations' ]
            }
          }]
        ]
      },
      'sources': [
        '<@(cares_sources_common)',
      ],
      'conditions': [
        [ 'library=="static_library"', {
          'defines': [ 'CARES_STATICLIB' ]
        }, {
          'defines': [ 'CARES_BUILDING_LIBRARY' ]
        }],
        [ 'OS=="win"', {
          'defines': [
            'CARES_PULL_WS2TCPIP_H=1',
            '_WINSOCK_DEPRECATED_NO_WARNINGS',
          ],
          'include_dirs': [ 'config/win32' ],
          'sources': [
            '<@(cares_sources_win)',
          ],
          'libraries': [
            '-lws2_32.lib',
            '-liphlpapi.lib'
          ],
        }, {
          # Not Windows i.e. POSIX
          'cflags': [
            '-g',
            '-pedantic',
            '-Wall',
            '-Wextra',
            '-Wno-unused-parameter'
          ],
          'defines': [ 'HAVE_CONFIG_H' ],
        }],
        [ 'OS not in "win android"', {
          'cflags': [
            '--std=gnu11'
          ],
        }],
        [ 'OS=="linux"', {
          'include_dirs': [ 'config/linux' ],
          'sources': [ 'config/linux/ares_config.h' ]
        }],
        [ 'OS=="mac" or OS=="ios"', {
          'include_dirs': [ 'config/darwin' ],
          'sources': [
            '<@(cares_sources_mac)',
          ]
        }],
        [ 'OS=="freebsd" or OS=="dragonflybsd"', {
          'include_dirs': [ 'config/freebsd' ],
          'sources': [ 'config/freebsd/ares_config.h' ]
        }],
        [ 'OS=="openbsd"', {
          'include_dirs': [ 'config/openbsd' ],
          'sources': [ 'config/openbsd/ares_config.h' ]
        }],
        [ 'OS=="android"', {
          'include_dirs': [ 'config/android' ],
          'sources': [ 'config/android/ares_config.h' ],
        }],
        [ 'OS=="solaris"', {
          'include_dirs': [ 'config/sunos' ],
          'sources': [ 'config/sunos/ares_config.h' ],
          'direct_dependent_settings': {
            'libraries': [
              '-lsocket',
              '-lnsl'
            ]
          }
        }]
      ]
    }
  ]
}
