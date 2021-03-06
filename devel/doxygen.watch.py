from urllib import request
import re

data = request.urlopen('https://sourceforge.net/projects/doxygen/files/').read().decode('utf-8')
matches = re.findall(r'rel-([0-9\.]+)</span></a>\n\s*</th>\n\s*<td headers="files_date_h" class="opt"><abbr title="(....-..-..)', data)
releases = [{'version': match[0], 'released': match[1]} for match in matches]
