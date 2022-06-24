import React from "react";
import LoginForm from "../components/login";

class Welcome extends React.Component {
  // constructor() {
  //   super();
  //   this.state = {
  //     login: false,
  //     name: "",
  //     level: "",
  //     kpi: "",
  //     iframe: {}
  //   };
  //   this.handleSubmit = this.handleSubmit.bind(this);
  // }

  // handleSubmit() {
  //   localStorage.clear();
  //   window.location.reload();
  // }

  // componentDidMount() {
  //   let login = localStorage.getItem("login");
  //   if (login) {
  //     const user = JSON.parse(localStorage.getItem("user"))[0];
  //     let level = data.levels.filter(
  //       level => level.id === Number(user.level)
  //     )[0];
  //     let kpi = data.KPI.filter(kpi => kpi.id === Number(user.KPI))[0];
  //     this.setState({
  //       login: true,
  //       name: user.name,
  //       level: level.name,
  //       iframe: level.dashboard,
  //       kpi: kpi.name
  //     });
  //     console.log("logged in");
  //   } else {
  //     console.log("logged out");
  //   }
  // }

  render() {
    // console.log(this.state);
    // if (this.state.login == true) {
      // return (
      //   <>
      //     <div className="container">
      //       <div className="row justify-content-center">
      //         <h3 className="title">
      //           Welcome {this.state.name}, View {this.state.level} level
      //           dashboard!
      //         </h3>
      //       </div>

      //       <div className="row justify-content-center">
      //         <iframe
      //           width={this.state.iframe.width}
      //           height={this.state.iframe.height}
      //           src={this.state.iframe.src}
      //           frameborder={this.state.iframe.frameborder}
      //           allowFullScreen={this.state.iframe.allowFullScreen}
      //         ></iframe>
      //       </div>
      //       <style jsx>{`
      //         html,
      //         body,
      //         * {
      //           font-family: Work Sans;
      //         }
      //       `}</style>
      //     </div>
      //   </>
      // );
    // } else {
      return (
        <div className="container">
          <LoginForm />
        </div>
      );
    }
}

export default Welcome;
