#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(.*?)\W+.to:(.*?)\W+.flags:(.*?)\W+.\]/).join(',')
