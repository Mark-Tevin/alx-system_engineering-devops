#!/usr/bin/env ruby
# This script accepts one argument and pass it to a regular expression matching method
# The regular expression must match school
puts ARGV[0].scan(/School/).join
