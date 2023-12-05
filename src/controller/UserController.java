package com.example.demo.controller;

import com.example.demo.entity.User;
import com.example.demo.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/users")
public class UserController {

    @Autowired
    private UserRepository userRepository;

    @PostMapping
    public String createUser(@RequestBody User user) {
        userRepository.save(user);
        return "User created successfully";
    }

    @GetMapping
    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    @DeleteMapping("/{username}")
    public String deleteUser(@PathVariable String username) {
        userRepository.deleteByUsername(username);
        return "User deleted successfully";
    }
}
