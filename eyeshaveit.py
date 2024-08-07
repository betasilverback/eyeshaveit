# main.py
#
# Copyright 2024 Phillip Stansell
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from mastodon import Mastodon
import tracery
import argparse
import json
import sys

pkgdatadir = '@pkgdatadir@'
sys.path.insert(1, pkgdatadir)

# init tracery
with open('scene.json') as rules_file:
  rules = json.load(rules_file)
grammar = tracery.Grammar(rules)

# init Mastodon
mastodon = Mastodon(
  #replace values/files with your own
  client_id = 'eyeshaveit_clientcred.secret',
  access_token = 'eyeshaveit_usercred.secret',
  api_base_url = 'https://stansells.org'
)

def eye_scene():
  """This function returns a random scene of spaces and eyes with a central 
     banana. The scene is nine characters wide by seven characters high. """
  return grammar.flatten("#origin#", allow_escape_chars=True)

def toot():
  """This function posts an eye_scene() to a Mastodon server."""
  mastodon.toot(eye_scene())
  
def console():
  """This function prints an eye_scene() to your console."""
  print(eye_scene())
  
def main(argv):
  """This program generates an eye_scene() for printing to your console and/or 
     posting to Mastodon."""
  parser = argparse.ArgumentParser(description='Create and output a scene with eyes.')
  parser.add_argument('-p', '--print', action='store_true', help='print to console')
  parser.add_argument('-t', '--toot', action='store_true', help='post to Mastodon')
  args = parser.parse_args()

  if args.toot:
    toot()
  if args.print:
    console()
  if (not args.print and not args.toot):
    console()

if __name__ == '__main__':
  sys.exit(main(sys.argv))

