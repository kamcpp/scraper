#!/bin/bash -x
PYTHONIOENCODING=UTF-8 python3 scrape.py | perl -wnE '$, = ","; say /([^>]*\.uk)[^&]*<span class="bid">€&nbsp;(\d+),-</g' | awk NF
