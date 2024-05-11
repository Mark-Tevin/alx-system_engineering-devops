#!/usr/bin/env ruby
# Expression must be exactly matching a string that starts with h ends with n
# can have any single character in between and accepts 
# one argument and pass it to a regular expression matching method

puts ARGV[0].scan(/^h.n$/).join
