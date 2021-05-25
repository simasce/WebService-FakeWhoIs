Examples for SOAP API queries
API link: http://localhost:5000/soap/
WSDL definition: http://localhost:5000/soap/?wsdl


list_whois_info() query example

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:who="whoisinfo.service">
   <soapenv:Header/>
   <soapenv:Body>
      <who:list_whois_info/>
   </soapenv:Body>
</soapenv:Envelope>



get_whois_info() query example

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:who="whoisinfo.service">
   <soapenv:Header/>
   <soapenv:Body>
      <who:get_whois_info>
         <who:id>1</who:id>
      </who:get_whois_info>
   </soapenv:Body>
</soapenv:Envelope>



delete_whois_info() query example

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:who="whoisinfo.service">
   <soapenv:Header/>
   <soapenv:Body>
      <who:delete_whois_info>
         <who:id>100</who:id>
      </who:delete_whois_info>
   </soapenv:Body>
</soapenv:Envelope>



update_whois_info() query example

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:who="whoisinfo.service" xmlns:who1="whois_info" xmlns:con="contact">
   <soapenv:Header/>
   <soapenv:Body>
      <who:update_whois_info>
         <who:id>1</who:id>
         <who:wInfo>
            <who1:id>1</who1:id>
            <who1:website>https://www.fighclub.net</who1:website>
            <who1:ipaddress>52.14.128.122</who1:ipaddress>
            <who1:contacts>
               <con:Contact>
                  <con:id>102</con:id>
                  <con:surname>Durden</con:surname>
                  <con:name>Tyler</con:name>
                  <con:number>(288) 555-0153</con:number>
                  <con:email>tyler@fightclub.net</con:email>
               </con:Contact>
            </who1:contacts>
         </who:wInfo>
      </who:update_whois_info>
   </soapenv:Body>
</soapenv:Envelope>



add_whois_info() query example

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:who="whoisinfo.service" xmlns:who1="whois_info" xmlns:con="contact">
   <soapenv:Header/>
   <soapenv:Body>
      <who:add_whois_info>
         <who:wInfo>
            <who1:id>100</who1:id>
            <who1:website>https://www.fightclub.com</who1:website>
            <who1:ipaddress>52.14.128.122</who1:ipaddress>
            <who1:contacts>
               <con:Contact>
                  <con:id>102</con:id>
                  <con:surname>Durden</con:surname>
                  <con:name>Tyler</con:name>
                  <con:number>(288) 555-0153</con:number>
                  <con:email>tyler@fightclub.com</con:email>
               </con:Contact>
            </who1:contacts>
         </who:wInfo>
      </who:add_whois_info>
   </soapenv:Body>
</soapenv:Envelope>



