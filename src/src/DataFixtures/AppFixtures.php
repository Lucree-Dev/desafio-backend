<?php

namespace App\DataFixtures;

use App\Entity\Person;
use Doctrine\Bundle\FixturesBundle\Fixture;
use Doctrine\Persistence\ObjectManager;

class AppFixtures extends Fixture
{
    public function load(ObjectManager $manager): void
    {
        $person = new Person();
        $person
            ->setFirstName('João')
            ->setLastName('da Silva')
            ->setBirthday(new \DateTime())
            ->setUsername('joao')
            ->setPassword(123)
        ;
        $manager->persist($person);

        $manager->flush();
    }
}
