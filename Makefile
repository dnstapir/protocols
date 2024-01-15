GENERATED=	events-mqtt-message.json \
		edge-configuration.json


validate: $(GENERATED)
	ajv --spec=draft2019 --strict=false compile -s $<

events-mqtt-message.json: events-mqtt-message.yaml
	 yq . < $< -o json > $@

edge-configuration.json: edge-configuration.yaml
	 yq . < $< -o json > $@

clean:
	rm -f $(GENERATED)
