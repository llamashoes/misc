require 'watir'
require 'win32/screenshot'
require "win32ole"

au3 = WIN32OLE.new("AutoItX3.Control")

# Open Browser
ie = Watir::IE.new
sleep 2

au3.WinActivate("ElfQuest")

ie.maximize
issue = 7
vols = 35
i = 1
while i <= vols
  puts i
  page = i
  if i <=9 
    page = "0"+i.to_s
  end
  ie.goto("http://elfquest.com/comic_viewer.php?fd=/gallery/OnlineComics/OQ/OQ0#{issue}/_Original%20ElfQuest%20-%20#{issue}_page=##{i}#_#{i}")
  sleep 8
  #Win32::Screenshot::Take.of(:window, :title => /internet/i, :area =>[608, 95, 1250, 1058]).write("#{issue}_image#{page}.jpg")
  Win32::Screenshot::Take.of(:window, :title => /internet/i, :area =>[580, 95, 1285, 1058]).write("#{issue}_image#{page}.jpg")

  #sleep 2
  i = i + 1
end

ie.close