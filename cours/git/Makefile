git.html: git.ipynb
	jupyter nbconvert --to=html git.ipynb

draw:
	git-draw -w project -g project/.git -p|dot -Tpdf -o project.pdf

TOKEN=$$(cat ../../../codeberg.tok)

get-project:
	curl -s -X "GET" \
		-H 'accept: application/json' \
  	"https://codeberg.org/api/v1/repos/fpom/project?token=$(TOKEN)" \
 	| jq

delete-project:
	curl -s -X "DELETE" \
  	-H 'accept: application/json' \
		"https://codeberg.org/api/v1/repos/fpom/project?token=$(TOKEN)" \
	| jq

create-project:
	curl -s -X "POST" \
		-H 'accept: application/json' \
		-H 'Content-Type: application/json' \
		-d '{"auto_init": false, "default_branch": "main", "description": "My nice project", "name": "project", "private": true, "template": false}' \
		"https://codeberg.org/api/v1/user/repos/?token=$(TOKEN)" \
	| jq

add-fpombis:
	curl -s -X "PUT" \
		-H 'accept: application/json' \
		-H 'Content-Type: application/json' \
		-d '{"permission": "read"}' \
		"https://codeberg.org/api/v1/repos/fpom/project/collaborators/fpombis?token=$(TOKEN)" \
	| jq

list-collaborators:
	curl -s -X "GET" \
		-H 'accept: application/json' \
		"https://codeberg.org/api/v1/repos/fpom/project/collaborators?page=1&limit=1000&token=$(TOKEN)" \
	| jq '.[].login'
