package com.RackSystemApplication.Controller;
import com.RackSystemApplication.Entity.RackItem;
import com.RackSystemApplication.Repository.RackItemRepository;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/racks")
public class RackController {

    private final RackItemRepository rackRepository;

    public RackController(RackItemRepository rackRepository) {
        this.rackRepository = rackRepository;
    }

    @GetMapping
    public List<RackItem> getAll() {
        return rackRepository.findAll();
    }

    @PostMapping
    public RackItem addRackItem(@RequestBody RackItem item) {
        return rackRepository.save(item);
    }
}
