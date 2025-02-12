GENERATED=	events/new_qname.json \
		events/new_aggregate.json \
		edge-observations.json


all: $(GENERATED) validate

validate:
	for file in $(GENERATED) ; do \
		ajv --spec=draft2020 --strict=false compile -s $$file ;\
	done

%.json: %.yaml
	 yq . < $< -o json > $@

clean:
	rm -f $(GENERATED)
