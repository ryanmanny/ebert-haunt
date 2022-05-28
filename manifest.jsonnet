local icon(size) =
  local iconsDir = 'icons/';
  local iconFileType = '.png';
  local iconFilePrefix = 'star-';

  iconsDir + iconFilePrefix + size + iconFileType;


local content_script(paths, scripts) =
  local host = '*://www.rogerebert.com/';
  local scriptsDir = 'scripts/';
  {
    'matches': [host + path for path in paths],
    'js': [scriptsDir + script for script in scripts],
  };


function(browser, version) {
  local manifestVersion =
    if std.asciiLower(browser) == 'chrome' then 3 else 2,

  'manifest_version': manifestVersion,
  'name': "Ebert Haunt",
  'version': version,
  'description': "Roger Ebert Lives Again!",
  'icons': {
    [size]: icon(size)
    for size in ['48', '96', '128']
  },
  'content_scripts': [
    content_script(
      [''],
      ['homepage.js', 'reviews-list.js'],
    ),
    content_script(
      ['reviews', 'collections/*'],
      ['reviews-list.js'],
    ),
    content_script(
      ['collections'],
      ['collections-list.js'],
    ),
    content_script(
      ['reviews/*'],
      ['review.js'],
    ),
  ]
}
