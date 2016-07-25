{
	"targets": [
		{
			"target_name": "fingerprint",
			"sources": [ "src/enroll.cpp", "src/verify.cpp", "src/identify.cpp", "src/fingerprint.cpp" ],
			"include_dirs": [
				"<!(node -e \"require('nan')\")",
				"<!(pkg-config --cflags zlib)",
				"-I/usr/include"
			],
			"libraries": [
				"<!(pkg-config --libs-only-l zlib)",
				"-L/usr/include -lfprint"
			],
			"variables": {
				"node_version": '<!(node --version | sed -e "s/^v\([0-9]*\\.[0-9]*\).*$/\\1/")',
			},
			"target_conditions": [
				[ "node_version == '0.10'", { "defines": ["OLD_UV_RUN_SIGNATURE"] } ]
			],
			"cflags": [
				"-I/usr/include"
			],
			"ldflags": [
				"-L/usr/lib -lfprint"
			]
		}
	],
}
