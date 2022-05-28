package controllers;

import com.google.gson.Gson;

import io.javalin.http.Handler;
import models.User;
import services.UserService;

import java.util.List;

    public class UserController {

        private UserService us;
        private Gson gson = new Gson();

        public UserController(UserService us) {
            this.us = us;
        }

        public Handler getAllUsers = (context) -> {

            List<User> users = us.getAllUsers();
            String usersJSON = gson.toJson(users);
            context.result(usersJSON);

        };

        public Handler getUser = (context) -> {

            int userId = Integer.parseInt(context.pathParam("userId"));
            User u = us.getUser(userId);
            context.result(gson.toJson(u));

        };
        public Handler createUser = (context) -> {

            User u = gson.fromJson(context.body(), User.class);

            u = us.addUser(u);
            context.result(gson.toJson(u));

        };

        public Handler updateUser = (context) -> {

            int userId = Integer.parseInt(context.pathParam("userId"));

            User change = gson.fromJson(context.body(), User.class);
            change.setUserId(userId);

            change = us.updateUser(change);
            context.result(gson.toJson(change));

        };

        public Handler deleteUser = (context) -> {

            int userId = Integer.parseInt(context.pathParam("userId"));
            User u = us.deleteUser(userId);
//        context.result(gson.toJson(u));

        };

    }

