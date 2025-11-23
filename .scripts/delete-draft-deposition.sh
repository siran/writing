set -e

DEPOSITION_ID=$1

curl -X DELETE \
  -H "Authorization: Bearer $ZENODO_TOKEN" \
  "https://zenodo.org/api/deposit/depositions/$DEPOSITION_ID"
