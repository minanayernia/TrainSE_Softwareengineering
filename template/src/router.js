import Vue from "vue";
import VueRouter from "vue-router";
import AuthGuard from "./utils/auth.guard";
import { adminRoot } from "./constants/config";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    redirect: `${adminRoot}/home`
  },
  {
    path: adminRoot,
    component: () => import("./views/app"),
    redirect: `${adminRoot}/home`,
    children: [
      {
        path: "home",
        component: () => import("./views/app/home")
      },
      {
        path: "resourceList/:id",
        name: "resource-list",
        component: () => import("./views/app/resourceList")
      },
      {
        path: "resourceDetail/:id",
        component: () => import("./views/app/resourceDetail")
      },
      {
        path: "notification",
        component: () => import("./views/app/notification")
      },
      {
        path: "profile",
        component: () => import("./views/app/profile")
      }
    ]
  },
  {
    path: "/error",
    component: () => import("./views/Error")
  },
  {
    path: "/user",
    component: () => import("./views/user"),
    redirect: "/user/login",
    children: [
      {
        path: "login",
        component: () => import("./views/user/Login")
      },
      {
        path: "register",
        component: () => import("./views/user/Register")
      }
    ]
  },
  {
    path: "*",
    component: () => import("./views/Error")
  }
];

const router = new VueRouter({
  linkActiveClass: "active",
  routes,
  mode: "history"
});
router.beforeEach(AuthGuard);
export default router;
