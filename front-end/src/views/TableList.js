/*!

=========================================================
* Black Dashboard React v1.2.1
=========================================================

* Product Page: https://www.creative-tim.com/product/black-dashboard-react
* Copyright 2022 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/black-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React from "react";

// reactstrap components
import {
  Card,
  CardHeader,
  CardBody,
  CardTitle,
  Table,
  Row,
  Col
} from "reactstrap";

function Tables() {
  return (
    <>
      <div className="content">
        <Row>
          <Col md="12">
            <Card>
              <CardHeader>
                <CardTitle tag="h4">Alerts</CardTitle>
              </CardHeader>
              <CardBody>
                <Table className="tablesorter" responsive>
                  <thead className="text-primary">
                    <tr>
                      <th>Date</th>
                      <th>Time</th>
                      <th>Type</th>
                      <th className="text-center">Notification Sent</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>2022.10.5</td>
                      <td>12:11 PM</td>
                      <td>Capacity Bound Alerts</td>
                      <td className="text-center">Sent</td>
                    </tr>
                    <tr>
                      <td>2022.10.4</td>
                      <td>10:22 PM</td>
                      <td>Capacity Bound Alerts</td>
                      <td className="text-center">Not Sent</td>
                    </tr>
                    <tr>
                      <td>2022.10.1</td>
                      <td>9:01 AM</td>
                      <td>Price Alerts</td>
                      <td className="text-center">Sent</td>
                    </tr>
                    <tr>
                      <td>2022.10.1</td>
                      <td>4:48 PM</td>
                      <td>Telecom Alerts</td>
                      <td className="text-center">Sent</td>
                    </tr>
                    <tr>
                      <td>2022.9.27</td>
                      <td>3:08 PM</td>
                      <td>Resource Depletion</td>
                      <td className="text-center">Sent</td>
                    </tr>
                    <tr>
                      <td>2022.9.24</td>
                      <td>11:11 AM</td>
                      <td>Capacity Bound Alerts</td>
                      <td className="text-center">Sent</td>
                    </tr>
                    <tr>
                      <td>2022.9.22</td>
                      <td>12:19 PM</td>
                      <td>Telecom Alerts</td>
                      <td className="text-center">Not Sent</td>
                    </tr>
                  </tbody>
                </Table>
              </CardBody>
            </Card>
          </Col>
          {/* <Col md="12">
            <Card className="card-plain">
              <CardHeader>
                <CardTitle tag="h4">Table on Plain Background</CardTitle>
                <p className="category">Here is a subtitle for this table</p>
              </CardHeader>
              <CardBody>
                <Table className="tablesorter" responsive>
                  <thead className="text-primary">
                    <tr>
                      <th>Name</th>
                      <th>Country</th>
                      <th>City</th>
                      <th className="text-center">Salary</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Dakota Rice</td>
                      <td>Niger</td>
                      <td>Oud-Turnhout</td>
                      <td className="text-center">$36,738</td>
                    </tr>
                    <tr>
                      <td>Minerva Hooper</td>
                      <td>Curaçao</td>
                      <td>Sinaai-Waas</td>
                      <td className="text-center">$23,789</td>
                    </tr>
                    <tr>
                      <td>Sage Rodriguez</td>
                      <td>Netherlands</td>
                      <td>Baileux</td>
                      <td className="text-center">$56,142</td>
                    </tr>
                    <tr>
                      <td>Philip Chaney</td>
                      <td>Korea, South</td>
                      <td>Overland Park</td>
                      <td className="text-center">$38,735</td>
                    </tr>
                    <tr>
                      <td>Doris Greene</td>
                      <td>Malawi</td>
                      <td>Feldkirchen in Kärnten</td>
                      <td className="text-center">$63,542</td>
                    </tr>
                    <tr>
                      <td>Mason Porter</td>
                      <td>Chile</td>
                      <td>Gloucester</td>
                      <td className="text-center">$78,615</td>
                    </tr>
                    <tr>
                      <td>Jon Porter</td>
                      <td>Portugal</td>
                      <td>Gloucester</td>
                      <td className="text-center">$98,615</td>
                    </tr>
                  </tbody>
                </Table>
              </CardBody>
            </Card>
          </Col> */}
        </Row>
      </div>
    </>
  );
}

export default Tables;
