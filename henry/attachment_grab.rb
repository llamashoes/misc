require 'rubygems'
require 'mail'

class Henry

# Connection information for local mailbox.
def local_connect
	local_mail = Mail.read('/var/mail/ryang')#('/Users/ryang/mbox')
end

# Connection info for remote mail server
def connect
	Mail.defaults do
   		retriever_method :imap, { :address             => "imap.gmail.com",
                          		  :port                => 993,
                             	  :user_name           => '',
                             	  :password            => '',
                             	  :enable_ssl          => true }
	end
end

# Checks for new mail and saves any attachments locally. Returns an array of local filepaths.
def remote_save_attachments
	# Can use this array to get the local filenames
	file_array = []
	mail = connect

	# Create mail objects and check new mail count
	all = mail.all
	puts "\nNew Mail: #{all.length}"
	if all.length == 0 
		exit
	else

	# If new mail exists scan each for attachments and save each attachment locally to a file. 
	# Each local filename is then put into an array that can be used in other methods
	# to upload the data etc.
	all.each {|m| m.attachments.each {|a| 
		save(a)
		file_array << File.expand_path(a.filename)
		}
	}	
	end
	puts "Total Attachments: #{file_array.length}"
	return file_array
end

def local_save_attachments
	file_array = []
	mail = local_connect
end

def save(attachment)
		File.open(attachment.filename, 'w') {|f| 
			f.write attachment.body.decoded
			}
		puts "#{attachment.filename} Saved"
end

# This method uploads any files in the passed in array.
def upload(files)
	files.each {|f|
		puts "\nUploading: #{f}"
		#Upload code here....
		sleep 2
		puts "Done\n"
	}

end

end

mail = Henry.new
files = mail.remote_save_attachments
mail.upload(files)


