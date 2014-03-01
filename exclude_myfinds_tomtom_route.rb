#!/bin/ruby

require 'csv'
require 'nokogiri'

def parse_myfinds(doc)
  doc.root.elements.each do |node|
    parse_wpt(node)
  end
end

def parse_wpt(node)
  if node.node_name.eql? 'wpt'
    node.elements.each do |node|
      parse_gccode(node)
    end
  end
end

def parse_gccode(node)
  if node.node_name.eql? 'name'
    #puts "MY: " + node.text.to_s
    @myfinds << node.text.to_s
  end
end

def parse_csv(csv)
  csv.each do |row|
    #puts "CSV: " + row[2]
    @caches << row[2]
  end
end

def parse_csv_tomtom(csv)
  csv.each do |row|
    unless already_found(row[2])
      puts row[0] + "|" + row[1] + "|" + row[2] + "|" + row[3] + "|"
    end
  end
end

def already_found(gccode)
  @myfinds.each do |find|
    if find.eql? gccode
      return true
    end
  end
  return false
end

def output_notfound
  @notfound = @caches - @myfinds

  @notfound.each do |cache|
    #puts "NOT: " + cache.to_s
    puts cache.to_s
  end
end

@myfinds = Array.new
@caches = Array.new
@notfound = Array.new

# open and parse myfinds gpx file
my = Nokogiri::XML(File.open("6086044.gpx"))
parse_myfinds(my)

# open and parse csv file
csvFile = File.read('route.csv')
csv = CSV.parse(csvFile, :headers => false, :col_sep => '|')
#parse_csv(csv)

# parse and output tomtom file
parse_csv_tomtom(csv)

# output the notfound caches
#output_notfound
