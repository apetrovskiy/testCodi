package testCodi_test

import (
	"testing"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

func TestTestCodi(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "TestCodi Suite")
}
