PIPE_DIR=/tmp/lucree.setup.lock
arr=("-" "\\" "|" "/" "-" "\\"  "|" "/")

close(){
  rm $PIPE_DIR
  exit
}

error(){
  #If there's no args
  if [ -z "$1" ]
  then
    return
  fi

  #Show a custom output
  echo -e "$(tput bold)$(tput setaf 1)- ERROR: $1 $(tput sgr0)"
  #Remove FIFO from tmp
  exit 1
}

spin(){
  n=0
  while true; do
    #Here read waiting (no_blocking) 250ms
    read -t 0.250 -r line < $PIPE_DIR
    #If there's a response from FIFO
    if [ ! -z "$line" ]
    then
      echo $line > $PIPE_DIR
      return
    fi

    #Below show a simple loading
    echo -ne "\r$(tput setaf 4) $(tput bold) ${arr[n]} Installing$(tput sgr0)"
    n=$(((n+1) % ${#arr[@]}))

    if [[ $n -eq ${#arr[@]} ]]
    then
      n=0
    fi
  done
}

goget(){
  # If there's no args
  if [ -z "$1" ]
  then
    error "Missing go package"
  fi

  #Save cursor position
  echo -e "$(tput setaf 3)Installing $2 (https://$1)$(tput sgr0)"
  tput sc
  #Running process getting in concurrency
  ( 
    #Show Spin
    spin $1
  ) &
  ( `go get -u $1` && echo yes || echo no ) > $PIPE_DIR
  
  < $PIPE_DIR

  tput rc
  tput ed
  #! `go get -u $1` && error "Install $1"
  echo -e "$(tput setaf 2)+ $2 Installed"
}

setup() {
  if [ -e $PIPE_DIR ]
  then
    echo "$(tput setaf 3) Case last script had interrupted, use rm $PIPE_DIR $(tput sgr0)"
    error "Another setup script is running, it was interrupted"
  fi

  #Create a fifo to communication between the processes
  mkfifo $PIPE_DIR

  echo "Author: Paulo Rodrigues Camacan"
  echo "Install all necessary components to run"

  echo "Installing Go packages"
  goget "github.com/go-chi/chi" "GoChi"
  goget "github.com/go-chi/jwtauth" "GoChi-JWT"
  goget "github.com/dgrijalva/jwt-go" "GO-JWT"
  goget "github.com/go-chi/render" "GoChi-Render"
  goget "gopkg.in/go-playground/validator.v9" "Validator"
  goget "gopkg.in/rethinkdb/rethinkdb-go.v6" "RethinkdbDriver"
  echo "$(tput bold)$(tput setaf 2)ALL PACKAGES INSTALLED!$(tput sgr0)"
  close
}

#Call setup method
setup